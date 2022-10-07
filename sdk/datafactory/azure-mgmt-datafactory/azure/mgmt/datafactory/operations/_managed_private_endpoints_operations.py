# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_by_factory_request(
    resource_group_name: str, factory_name: str, managed_virtual_network_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
        "managedVirtualNetworkName": _SERIALIZER.url(
            "managed_virtual_network_name",
            managed_virtual_network_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(
    resource_group_name: str,
    factory_name: str,
    managed_virtual_network_name: str,
    managed_private_endpoint_name: str,
    subscription_id: str,
    *,
    if_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))  # type: str
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints/{managedPrivateEndpointName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
        "managedVirtualNetworkName": _SERIALIZER.url(
            "managed_virtual_network_name",
            managed_virtual_network_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
        "managedPrivateEndpointName": _SERIALIZER.url(
            "managed_private_endpoint_name",
            managed_private_endpoint_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if if_match is not None:
        _headers["If-Match"] = _SERIALIZER.header("if_match", if_match, "str")
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    resource_group_name: str,
    factory_name: str,
    managed_virtual_network_name: str,
    managed_private_endpoint_name: str,
    subscription_id: str,
    *,
    if_none_match: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints/{managedPrivateEndpointName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
        "managedVirtualNetworkName": _SERIALIZER.url(
            "managed_virtual_network_name",
            managed_virtual_network_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
        "managedPrivateEndpointName": _SERIALIZER.url(
            "managed_private_endpoint_name",
            managed_private_endpoint_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if if_none_match is not None:
        _headers["If-None-Match"] = _SERIALIZER.header("if_none_match", if_none_match, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_delete_request(
    resource_group_name: str,
    factory_name: str,
    managed_virtual_network_name: str,
    managed_private_endpoint_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2018-06-01"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints/{managedPrivateEndpointName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1, pattern=r"^[-\w\._\(\)]+$"
        ),
        "factoryName": _SERIALIZER.url(
            "factory_name",
            factory_name,
            "str",
            max_length=63,
            min_length=3,
            pattern=r"^[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*$",
        ),
        "managedVirtualNetworkName": _SERIALIZER.url(
            "managed_virtual_network_name",
            managed_virtual_network_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
        "managedPrivateEndpointName": _SERIALIZER.url(
            "managed_private_endpoint_name",
            managed_private_endpoint_name,
            "str",
            max_length=127,
            min_length=1,
            pattern=r"^([_A-Za-z0-9]|([_A-Za-z0-9][-_A-Za-z0-9]{0,125}[_A-Za-z0-9]))$",
        ),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


class ManagedPrivateEndpointsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.datafactory.DataFactoryManagementClient`'s
        :attr:`managed_private_endpoints` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list_by_factory(
        self, resource_group_name: str, factory_name: str, managed_virtual_network_name: str, **kwargs: Any
    ) -> Iterable["_models.ManagedPrivateEndpointResource"]:
        """Lists managed private endpoints.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param managed_virtual_network_name: Managed virtual network name. Required.
        :type managed_virtual_network_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ManagedPrivateEndpointResource or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ManagedPrivateEndpointListResponse]

        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_by_factory_request(
                    resource_group_name=resource_group_name,
                    factory_name=factory_name,
                    managed_virtual_network_name=managed_virtual_network_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_by_factory.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urlparse(next_link)
                _next_request_params = case_insensitive_dict(parse_qs(_parsed_next_link.query))
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest("GET", urljoin(next_link, _parsed_next_link.path), params=_next_request_params)
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ManagedPrivateEndpointListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list_by_factory.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints"}  # type: ignore

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        managed_virtual_network_name: str,
        managed_private_endpoint_name: str,
        managed_private_endpoint: _models.ManagedPrivateEndpointResource,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedPrivateEndpointResource:
        """Creates or updates a managed private endpoint.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param managed_virtual_network_name: Managed virtual network name. Required.
        :type managed_virtual_network_name: str
        :param managed_private_endpoint_name: Managed private endpoint name. Required.
        :type managed_private_endpoint_name: str
        :param managed_private_endpoint: Managed private endpoint resource definition. Required.
        :type managed_private_endpoint: ~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource
        :param if_match: ETag of the managed private endpoint entity. Should only be specified for
         update, for which it should match existing entity or can be * for unconditional update. Default
         value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedPrivateEndpointResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        managed_virtual_network_name: str,
        managed_private_endpoint_name: str,
        managed_private_endpoint: IO,
        if_match: Optional[str] = None,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ManagedPrivateEndpointResource:
        """Creates or updates a managed private endpoint.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param managed_virtual_network_name: Managed virtual network name. Required.
        :type managed_virtual_network_name: str
        :param managed_private_endpoint_name: Managed private endpoint name. Required.
        :type managed_private_endpoint_name: str
        :param managed_private_endpoint: Managed private endpoint resource definition. Required.
        :type managed_private_endpoint: IO
        :param if_match: ETag of the managed private endpoint entity. Should only be specified for
         update, for which it should match existing entity or can be * for unconditional update. Default
         value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedPrivateEndpointResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        managed_virtual_network_name: str,
        managed_private_endpoint_name: str,
        managed_private_endpoint: Union[_models.ManagedPrivateEndpointResource, IO],
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ManagedPrivateEndpointResource:
        """Creates or updates a managed private endpoint.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param managed_virtual_network_name: Managed virtual network name. Required.
        :type managed_virtual_network_name: str
        :param managed_private_endpoint_name: Managed private endpoint name. Required.
        :type managed_private_endpoint_name: str
        :param managed_private_endpoint: Managed private endpoint resource definition. Is either a
         model type or a IO type. Required.
        :type managed_private_endpoint: ~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource
         or IO
        :param if_match: ETag of the managed private endpoint entity. Should only be specified for
         update, for which it should match existing entity or can be * for unconditional update. Default
         value is None.
        :type if_match: str
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedPrivateEndpointResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ManagedPrivateEndpointResource]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(managed_private_endpoint, (IO, bytes)):
            _content = managed_private_endpoint
        else:
            _json = self._serialize.body(managed_private_endpoint, "ManagedPrivateEndpointResource")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            managed_virtual_network_name=managed_virtual_network_name,
            managed_private_endpoint_name=managed_private_endpoint_name,
            subscription_id=self._config.subscription_id,
            if_match=if_match,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ManagedPrivateEndpointResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints/{managedPrivateEndpointName}"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name: str,
        factory_name: str,
        managed_virtual_network_name: str,
        managed_private_endpoint_name: str,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> _models.ManagedPrivateEndpointResource:
        """Gets a managed private endpoint.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param managed_virtual_network_name: Managed virtual network name. Required.
        :type managed_virtual_network_name: str
        :param managed_private_endpoint_name: Managed private endpoint name. Required.
        :type managed_private_endpoint_name: str
        :param if_none_match: ETag of the managed private endpoint entity. Should only be specified for
         get. If the ETag matches the existing entity tag, or if * was provided, then no content will be
         returned. Default value is None.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ManagedPrivateEndpointResource or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.ManagedPrivateEndpointResource
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ManagedPrivateEndpointResource]

        request = build_get_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            managed_virtual_network_name=managed_virtual_network_name,
            managed_private_endpoint_name=managed_private_endpoint_name,
            subscription_id=self._config.subscription_id,
            if_none_match=if_none_match,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ManagedPrivateEndpointResource", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints/{managedPrivateEndpointName}"}  # type: ignore

    @distributed_trace
    def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        factory_name: str,
        managed_virtual_network_name: str,
        managed_private_endpoint_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a managed private endpoint.

        :param resource_group_name: The resource group name. Required.
        :type resource_group_name: str
        :param factory_name: The factory name. Required.
        :type factory_name: str
        :param managed_virtual_network_name: Managed virtual network name. Required.
        :type managed_virtual_network_name: str
        :param managed_private_endpoint_name: Managed private endpoint name. Required.
        :type managed_private_endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", self._config.api_version))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            managed_virtual_network_name=managed_virtual_network_name,
            managed_private_endpoint_name=managed_private_endpoint_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/managedVirtualNetworks/{managedVirtualNetworkName}/managedPrivateEndpoints/{managedPrivateEndpointName}"}  # type: ignore
