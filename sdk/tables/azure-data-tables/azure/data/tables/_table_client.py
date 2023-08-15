# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import functools
from typing import Optional, Any, Union, List, Dict, Mapping, Iterable, overload, cast

try:
    from urllib.parse import urlparse, unquote
except ImportError:
    from urlparse import urlparse  # type: ignore
    from urllib2 import unquote  # type: ignore

from azure.core import MatchConditions
from azure.core.credentials import AzureNamedKeyCredential, AzureSasCredential, TokenCredential
from azure.core.exceptions import HttpResponseError
from azure.core.paging import ItemPaged
from azure.core.tracing.decorator import distributed_trace

from ._base_client import parse_connection_str, TablesBaseClient
from ._entity import TableEntity
from ._error import (
    _decode_error,
    _process_table_error,
    _reprocess_error,
    _validate_tablename_error,
    _validate_key_values,
)
from ._generated.models import SignedIdentifier, TableProperties
from ._serialize import (
    serialize_iso,
    _parameter_filter_substitution,
    _get_match_headers,
    _add_entity_properties,
    _prepare_key,
)
from ._deserialize import deserialize_iso, _return_headers_and_deserialized, _convert_to_entity, _trim_service_metadata
from ._table_batch import TableBatchOperations, EntityType, TransactionOperationType
from ._models import TableEntityPropertiesPaged, UpdateMode, TableAccessPolicy, TableItem


class TableClient(TablesBaseClient):
    """A client to interact with a specific Table in an Azure Tables account.

    :ivar str account_name: The name of the Tables account.
    :ivar str table_name: The name of the table.
    :ivar str scheme: The scheme component in the full URL to the Tables account.
    :ivar str url: The storage endpoint.
    :ivar str api_version: The service API version.
    """

    def __init__(  # pylint: disable=missing-client-constructor-parameter-credential
        self,
        endpoint: str,
        table_name: str,
        *,
        credential: Optional[Union[AzureSasCredential, AzureNamedKeyCredential, TokenCredential]] = None,
        **kwargs,
    ) -> None:
        """Create TableClient from a Credential.

        :param str endpoint: A URL to an Azure Tables account.
        :param str table_name: The table name.
        :keyword credential:
            The credentials with which to authenticate. This is optional if the
            account URL already has a SAS token. The value can be one of AzureNamedKeyCredential (azure-core),
            AzureSasCredential (azure-core), or a TokenCredential implementation from azure-identity.
        :paramtype credential:
            ~azure.core.credentials.AzureNamedKeyCredential or
            ~azure.core.credentials.AzureSasCredential or
            ~azure.core.credentials.TokenCredential or None
        :keyword api_version: Specifies the version of the operation to use for this request. Default value
            is "2019-02-02".
        :paramtype api_version: str
        :returns: None
        """
        if not table_name:
            raise ValueError("Please specify a table name.")
        self.table_name = table_name
        super(TableClient, self).__init__(endpoint, credential=credential, **kwargs)

    def _format_url(self, hostname):
        """Format the endpoint URL according to the current location
        mode hostname.

        :param str hostname: The current location mode hostname.
        :returns: The full URL to the Tables account.
        :rtype: str
        """
        return f"{self.scheme}://{hostname}{self._query_str}"

    @classmethod
    def from_connection_string(cls, conn_str: str, table_name: str, **kwargs) -> "TableClient":
        """Create TableClient from a Connection String.

        :param str conn_str: A connection string to an Azure Tables account.
        :param str table_name: The table name.
        :returns: A table client.
        :rtype: ~azure.data.tables.TableClient

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_create_client.py
                :start-after: [START create_table_client]
                :end-before: [END create_table_client]
                :language: python
                :dedent: 8
                :caption: Authenticating a TableServiceClient from a connection_string
        """
        endpoint, credential = parse_connection_str(conn_str=conn_str, credential=None, keyword_args=kwargs)
        return cls(endpoint, table_name=table_name, credential=credential, **kwargs)

    @classmethod
    def from_table_url(
        cls,
        table_url: str,
        *,
        credential: Optional[Union[AzureNamedKeyCredential, AzureSasCredential]] = None,
        **kwargs,
    ) -> "TableClient":
        """A client to interact with a specific Table.

        :param str table_url: The full URI to the table, including SAS token if used.
        :keyword credential:
            The credentials with which to authenticate. This is optional if the
            account URL already has a SAS token. The value can be one of AzureNamedKeyCredential (azure-core),
        AzureSasCredential (azure-core), or a TokenCredential implementation from azure-identity.
        :paramtype credential:
            ~azure.core.credentials.AzureNamedKeyCredential or
            ~azure.core.credentials.AzureSasCredential or None
        :returns: A table client.
        :rtype: ~azure.data.tables.TableClient
        """
        try:
            if not table_url.lower().startswith("http"):
                table_url = "https://" + table_url
        except AttributeError as exc:
            raise ValueError("Table URL must be a string.") from exc
        parsed_url = urlparse(table_url.rstrip("/"))

        if not parsed_url.netloc:
            raise ValueError(f"Invalid URL: {table_url}")

        table_path = parsed_url.path.lstrip("/").split("/")
        account_path = ""
        if len(table_path) > 1:
            account_path = "/" + "/".join(table_path[:-1])
        endpoint = f"{parsed_url.scheme}://{parsed_url.netloc.rstrip('/')}{account_path}?{parsed_url.query}"
        table_name = unquote(table_path[-1])
        if table_name.lower().startswith("tables('"):
            table_name = table_name[8:-2]
        if not table_name:
            raise ValueError("Invalid URL. Please provide a URL with a valid table name")
        return cls(endpoint, table_name=table_name, credential=credential, **kwargs)

    @distributed_trace
    def get_table_access_policy(self, **kwargs) -> Dict[str, Optional[TableAccessPolicy]]:
        """Retrieves details about any stored access policies specified on the table that may be
        used with Shared Access Signatures.

        :return: Dictionary of SignedIdentifiers
        :rtype: dict[str, ~azure.data.tables.TableAccessPolicy] or dict[str, None]
        :raises: :class:`~azure.core.exceptions.HttpResponseError`
        """
        timeout = kwargs.pop("timeout", None)
        try:
            _, identifiers = self._client.table.get_access_policy(
                table=self.table_name,
                timeout=timeout,
                cls=kwargs.pop("cls", None) or _return_headers_and_deserialized,
                **kwargs,
            )
        except HttpResponseError as error:
            _process_table_error(error, table_name=self.table_name)
        output = {}  # type: Dict[str, Optional[TableAccessPolicy]]
        for identifier in cast(List[SignedIdentifier], identifiers):
            if identifier.access_policy:
                output[identifier.id] = TableAccessPolicy(
                    start=deserialize_iso(identifier.access_policy.start),
                    expiry=deserialize_iso(identifier.access_policy.expiry),
                    permission=identifier.access_policy.permission,
                )
            else:
                output[identifier.id] = None
        return output

    @distributed_trace
    def set_table_access_policy(self, signed_identifiers: Dict[str, Optional[TableAccessPolicy]], **kwargs) -> None:
        """Sets stored access policies for the table that may be used with Shared Access Signatures.

        :param signed_identifiers: Access policies to set for the table
        :type signed_identifiers: dict[str, ~azure.data.tables.TableAccessPolicy] or dict[str, None]
        :return: None
        :raises: :class:`~azure.core.exceptions.HttpResponseError`
        """
        identifiers = []
        for key, value in signed_identifiers.items():
            payload = None
            if value:
                payload = TableAccessPolicy(
                    start=serialize_iso(value.start), expiry=serialize_iso(value.expiry), permission=value.permission
                )
            identifiers.append(SignedIdentifier(id=key, access_policy=payload))
        try:
            self._client.table.set_access_policy(
                table=self.table_name, table_acl=identifiers or None, **kwargs  # type: ignore
            )
        except HttpResponseError as error:
            try:
                _process_table_error(error, table_name=self.table_name)
            except HttpResponseError as table_error:
                _reprocess_error(table_error, identifiers=identifiers)
                raise

    @distributed_trace
    def create_table(self, **kwargs) -> TableItem:
        """Creates a new table under the current account.

        :return: A TableItem representing the created table.
        :rtype: ~azure.data.tables.TableItem
        :raises: :class:`~azure.core.exceptions.ResourceExistsError` If the entity already exists

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_create_delete_table.py
                :start-after: [START create_table_from_table_client]
                :end-before: [END create_table_from_table_client]
                :language: python
                :dedent: 8
                :caption: Creating a table from the TableClient object
        """
        table_properties = TableProperties(table_name=self.table_name)
        try:
            result = self._client.table.create(table_properties, **kwargs)
        except HttpResponseError as error:
            try:
                _process_table_error(error, table_name=self.table_name)
            except HttpResponseError as decoded_error:
                _reprocess_error(decoded_error)
                raise
        return TableItem(name=result.table_name)  # type: ignore

    @distributed_trace
    def delete_table(self, **kwargs) -> None:
        """Deletes the table under the current account. No error will be raised
        if the table does not exist

        :return: None
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_create_delete_table.py
                :start-after: [START delete_table_from_table_client]
                :end-before: [END delete_table_from_table_client]
                :language: python
                :dedent: 8
                :caption: Deleting a table from the TableClient object
        """
        try:
            self._client.table.delete(table=self.table_name, **kwargs)
        except HttpResponseError as error:
            if error.status_code == 404:
                return
            try:
                _process_table_error(error, table_name=self.table_name)
            except HttpResponseError as decoded_error:
                _reprocess_error(decoded_error)
                raise

    @overload
    def delete_entity(self, partition_key: str, row_key: str, **kwargs) -> None:
        pass

    @overload
    def delete_entity(self, entity: Union[TableEntity, Mapping[str, Any]], **kwargs) -> None:
        pass

    @distributed_trace
    def delete_entity(self, *args: Union[TableEntity, str], **kwargs) -> None:
        """Deletes the specified entity in a table. No error will be raised if
        the entity or PartitionKey-RowKey pairing is not found.

        :param str partition_key: The partition key of the entity.
        :param str row_key: The row key of the entity.
        :param entity: The entity to delete
        :type entity: Union[TableEntity, Mapping[str, str]]
        :keyword str etag: Etag of the entity
        :keyword match_condition: The condition under which to perform the operation.
            Supported values include: MatchConditions.IfNotModified, MatchConditions.Unconditionally.
            The default value is Unconditionally.
        :paramtype match_condition: ~azure.core.MatchConditions
        :return: None
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_insert_delete_entities.py
                :start-after: [START delete_entity]
                :end-before: [END delete_entity]
                :language: python
                :dedent: 12
                :caption: Deleting an entity of a Table
        """
        try:
            entity = kwargs.pop("entity", None)
            if not entity:
                entity = args[0]
            partition_key = entity["PartitionKey"]
            row_key = entity["RowKey"]
        except (TypeError, IndexError):
            partition_key = kwargs.pop("partition_key", None)
            if partition_key is None:
                partition_key = args[0]
            row_key = kwargs.pop("row_key", None)
            if row_key is None:
                row_key = args[1]

        match_condition = kwargs.pop("match_condition", None)
        etag = kwargs.pop("etag", None)
        if match_condition and entity and not etag:
            try:
                etag = entity.metadata.get("etag", None)
            except (AttributeError, TypeError):
                pass
        if_match = _get_match_headers(
            etag=etag,
            match_condition=match_condition or MatchConditions.Unconditionally,
        )

        try:
            self._client.table.delete_entity(
                table=self.table_name,
                partition_key=_prepare_key(partition_key),
                row_key=_prepare_key(row_key),
                if_match=if_match,
                **kwargs,
            )
        except HttpResponseError as error:
            if error.status_code == 404:
                return
            _process_table_error(error, table_name=self.table_name)

    @distributed_trace
    def create_entity(self, entity: EntityType, **kwargs) -> Dict[str, Any]:
        """Insert entity in a table.

        :param entity: The properties for the table entity.
        :type entity: Union[TableEntity, Mapping[str, Any]]
        :return: Dictionary mapping operation metadata returned from the service
        :rtype: dict[str, Any]
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_insert_delete_entities.py
                :start-after: [START create_entity]
                :end-before: [END create_entity]
                :language: python
                :dedent: 12
                :caption: Creating and adding an entity to a Table
        """
        entity = _add_entity_properties(entity)
        try:
            metadata, content = self._client.table.insert_entity(  # type: ignore
                table=self.table_name,
                table_entity_properties=entity,  # type: ignore
                cls=kwargs.pop("cls", _return_headers_and_deserialized),
                **kwargs,
            )
        except HttpResponseError as error:
            decoded = _decode_error(error.response, error.message)
            _validate_key_values(decoded, entity.get("PartitionKey"), entity.get("RowKey"))
            _validate_tablename_error(decoded, self.table_name)
            # We probably should have been raising decoded error before removing _reraise_error()
            raise error
        return _trim_service_metadata(metadata, content=content)  # type: ignore

    @distributed_trace
    def update_entity(self, entity: EntityType, mode: UpdateMode = UpdateMode.MERGE, **kwargs) -> Dict[str, Any]:
        """Update entity in a table.

        :param entity: The properties for the table entity.
        :type entity: ~azure.data.tables.TableEntity or dict[str, Any]
        :param mode: Merge or Replace entity
        :type mode: ~azure.data.tables.UpdateMode
        :keyword str etag: Etag of the entity
        :keyword match_condition: The condition under which to perform the operation.
            Supported values include: MatchConditions.IfNotModified, MatchConditions.Unconditionally.
            The default value is Unconditionally.
        :paramtype match_condition: ~azure.core.MatchConditions
        :return: Dictionary mapping operation metadata returned from the service
        :rtype: dict[str, Any]
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_update_upsert_merge_entities.py
                :start-after: [START update_entity]
                :end-before: [END update_entity]
                :language: python
                :dedent: 16
                :caption: Updating an already exiting entity in a Table
        """
        match_condition = kwargs.pop("match_condition", None)
        etag = kwargs.pop("etag", None)
        if match_condition and not etag:
            try:
                etag = entity.metadata.get("etag", None)  # type: ignore
            except (AttributeError, TypeError):
                pass
        if_match = _get_match_headers(
            etag=etag,
            match_condition=match_condition or MatchConditions.Unconditionally,
        )
        entity = _add_entity_properties(entity)
        partition_key = entity["PartitionKey"]
        row_key = entity["RowKey"]
        try:
            metadata = None
            content = None
            if mode == UpdateMode.REPLACE:
                metadata, content = self._client.table.update_entity(  # type: ignore
                    table=self.table_name,
                    partition_key=_prepare_key(partition_key),
                    row_key=_prepare_key(row_key),
                    table_entity_properties=entity,  # type: ignore
                    if_match=if_match,
                    cls=kwargs.pop("cls", _return_headers_and_deserialized),
                    **kwargs,
                )
            elif mode == UpdateMode.MERGE:
                metadata, content = self._client.table.merge_entity(  # type: ignore
                    table=self.table_name,
                    partition_key=_prepare_key(partition_key),
                    row_key=_prepare_key(row_key),
                    if_match=if_match,
                    table_entity_properties=entity,  # type: ignore
                    cls=kwargs.pop("cls", _return_headers_and_deserialized),
                    **kwargs,
                )
            else:
                raise ValueError(f"Mode type '{mode}' is not supported.")
        except HttpResponseError as error:
            _process_table_error(error, table_name=self.table_name)
        return _trim_service_metadata(metadata, content=content)  # type: ignore

    @distributed_trace
    def list_entities(self, **kwargs) -> ItemPaged[TableEntity]:
        """Lists entities in a table.

        :keyword int results_per_page: Number of entities returned per service request.
        :keyword select: Specify desired properties of an entity to return.
        :paramtype select: str or list[str]
        :return: An iterator of :class:`~azure.data.tables.TableEntity`
        :rtype: ~azure.core.paging.ItemPaged[~azure.data.tables.TableEntity]
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_update_upsert_merge_entities.py
                :start-after: [START list_entities]
                :end-before: [END list_entities]
                :language: python
                :dedent: 16
                :caption: List all entities held within a table
        """
        user_select = kwargs.pop("select", None)
        if user_select and not isinstance(user_select, str):
            user_select = ",".join(user_select)
        top = kwargs.pop("results_per_page", None)

        command = functools.partial(self._client.table.query_entities, **kwargs)
        return ItemPaged(
            command,
            table=self.table_name,
            results_per_page=top,
            select=user_select,
            page_iterator_class=TableEntityPropertiesPaged,
        )

    @distributed_trace
    def query_entities(self, query_filter: str, **kwargs) -> ItemPaged[TableEntity]:
        # pylint: disable=line-too-long
        """Lists entities in a table.

        :param str query_filter: Specify a filter to return certain entities. For more information
         on filter formatting, see the `samples documentation <https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/tables/azure-data-tables/samples#writing-filters>`_.
        :keyword int results_per_page: Number of entities returned per service request.
        :keyword select: Specify desired properties of an entity to return.
        :paramtype select: str or list[str]
        :keyword parameters: Dictionary for formatting query with additional, user defined parameters
        :paramtype parameters: dict[str, Any]
        :return: An iterator of :class:`~azure.data.tables.TableEntity`
        :rtype: ~azure.core.paging.ItemPaged[~azure.data.tables.TableEntity]
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_query_table.py
                :start-after: [START query_entities]
                :end-before: [END query_entities]
                :language: python
                :dedent: 8
                :caption: Query entities held within a table
        """
        parameters = kwargs.pop("parameters", None)
        query_filter = _parameter_filter_substitution(parameters, query_filter)  # type: ignore
        top = kwargs.pop("results_per_page", None)
        user_select = kwargs.pop("select", None)
        if user_select and not isinstance(user_select, str):
            user_select = ",".join(user_select)  # type: ignore

        command = functools.partial(self._client.table.query_entities, **kwargs)
        return ItemPaged(
            command,
            table=self.table_name,
            results_per_page=top,
            filter=query_filter,
            select=user_select,
            page_iterator_class=TableEntityPropertiesPaged,
        )

    @distributed_trace
    def get_entity(self, partition_key: str, row_key: str, **kwargs) -> TableEntity:
        """Get a single entity in a table.

        :param partition_key: The partition key of the entity.
        :type partition_key: str
        :param row_key: The row key of the entity.
        :type row_key: str
        :keyword select: Specify desired properties of an entity to return.
        :paramtype select: str or list[str]
        :return: Dictionary mapping operation metadata returned from the service
        :rtype: ~azure.data.tables.TableEntity
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_update_upsert_merge_entities.py
                :start-after: [START get_entity]
                :end-before: [END get_entity]
                :language: python
                :dedent: 16
                :caption: Get a single entity from a table
        """
        user_select = kwargs.pop("select", None)
        if user_select and not isinstance(user_select, str):
            user_select = ",".join(user_select)
        try:
            entity = self._client.table.query_entity_with_partition_and_row_key(
                table=self.table_name,
                partition_key=_prepare_key(partition_key),
                row_key=_prepare_key(row_key),
                select=user_select,
                **kwargs,
            )
        except HttpResponseError as error:
            _process_table_error(error, table_name=self.table_name)
        return _convert_to_entity(entity)

    @distributed_trace
    def upsert_entity(self, entity: EntityType, mode: UpdateMode = UpdateMode.MERGE, **kwargs) -> Dict[str, Any]:
        """Update/Merge or Insert entity into table.

        :param entity: The properties for the table entity.
        :type entity: ~azure.data.tables.TableEntity or dict[str, Any]
        :param mode: Merge or Replace entity
        :type mode: ~azure.data.tables.UpdateMode
        :return: Dictionary mapping operation metadata returned from the service
        :rtype: dict[str, Any]
        :raises: :class:`~azure.core.exceptions.HttpResponseError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_update_upsert_merge_entities.py
                :start-after: [START upsert_entity]
                :end-before: [END upsert_entity]
                :language: python
                :dedent: 16
                :caption: Update/merge or insert an entity into a table
        """
        entity = _add_entity_properties(entity)
        partition_key = entity["PartitionKey"]
        row_key = entity["RowKey"]
        try:
            metadata = None
            content = None
            if mode == UpdateMode.MERGE:
                metadata, content = self._client.table.merge_entity(  # type: ignore
                    table=self.table_name,
                    partition_key=_prepare_key(partition_key),
                    row_key=_prepare_key(row_key),
                    table_entity_properties=entity,  # type: ignore
                    cls=kwargs.pop("cls", _return_headers_and_deserialized),
                    **kwargs,
                )
            elif mode == UpdateMode.REPLACE:
                metadata, content = self._client.table.update_entity(  # type: ignore
                    table=self.table_name,
                    partition_key=_prepare_key(partition_key),
                    row_key=_prepare_key(row_key),
                    table_entity_properties=entity,  # type: ignore
                    cls=kwargs.pop("cls", _return_headers_and_deserialized),
                    **kwargs,
                )
            else:
                raise ValueError(
                    f"Update mode {mode} is not supported. For a list of supported modes see the UpdateMode enum."
                )
        except HttpResponseError as error:
            _process_table_error(error, table_name=self.table_name)
        return _trim_service_metadata(metadata, content=content)  # type: ignore

    @distributed_trace
    def submit_transaction(self, operations: Iterable[TransactionOperationType], **kwargs) -> List[Mapping[str, Any]]:
        """Commit a list of operations as a single transaction.

        If any one of these operations fails, the entire transaction will be rejected.

        :param operations: The list of operations to commit in a transaction. This should be an iterable of
         tuples containing an operation name, the entity on which to operate, and optionally, a dict of additional
         kwargs for that operation. For example::

            - ('upsert', {'PartitionKey': 'A', 'RowKey': 'B'})
            - ('upsert', {'PartitionKey': 'A', 'RowKey': 'B'}, {'mode': UpdateMode.REPLACE})

        :type operations: Iterable[Tuple[str, TableEntity, Mapping[str, Any]]]
        :return: A list of mappings with response metadata for each operation in the transaction.
        :rtype: list[Mapping[str, Any]]
        :raises: :class:`~azure.data.tables.TableTransactionError`

        .. admonition:: Example:

            .. literalinclude:: ../samples/sample_batching.py
                :start-after: [START batching]
                :end-before: [END batching]
                :language: python
                :dedent: 8
                :caption: Using transactions to send multiple requests at once
        """
        batched_requests = TableBatchOperations(
            self._client,
            self._client._serialize,  # pylint: disable=protected-access
            self._client._deserialize,  # pylint: disable=protected-access
            self._client._config,  # pylint: disable=protected-access
            self.table_name,
            is_cosmos_endpoint=self._cosmos_endpoint,
            **kwargs,
        )
        try:
            for operation in operations:
                batched_requests.add_operation(operation)
        except TypeError as exc:
            raise TypeError(
                "The value of 'operations' must be an iterator "
                "of Tuples. Please check documentation for correct Tuple format."
            ) from exc
        return self._batch_send(self.table_name, *batched_requests.requests, **kwargs)  # type: ignore
