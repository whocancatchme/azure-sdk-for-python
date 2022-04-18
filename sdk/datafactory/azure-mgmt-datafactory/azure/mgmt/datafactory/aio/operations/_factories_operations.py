# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._factories_operations import build_configure_factory_repo_request, build_create_or_update_request, build_delete_request, build_get_data_plane_access_request, build_get_git_hub_access_token_request, build_get_request, build_list_by_resource_group_request, build_list_request, build_update_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class FactoriesOperations:
    """FactoriesOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.datafactory.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        **kwargs: Any
    ) -> AsyncIterable["_models.FactoryListResponse"]:
        """Lists factories under the specified subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FactoryListResponse or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.datafactory.models.FactoryListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FactoryListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FactoryListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/factories"}  # type: ignore

    @distributed_trace_async
    async def configure_factory_repo(
        self,
        location_id: str,
        factory_repo_update: "_models.FactoryRepoUpdate",
        **kwargs: Any
    ) -> "_models.Factory":
        """Updates a factory's repo information.

        :param location_id: The location identifier.
        :type location_id: str
        :param factory_repo_update: Update factory repo request definition.
        :type factory_repo_update: ~azure.mgmt.datafactory.models.FactoryRepoUpdate
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Factory, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.Factory
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Factory"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(factory_repo_update, 'FactoryRepoUpdate')

        request = build_configure_factory_repo_request(
            subscription_id=self._config.subscription_id,
            location_id=location_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.configure_factory_repo.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Factory', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    configure_factory_repo.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.DataFactory/locations/{locationId}/configureFactoryRepo"}  # type: ignore


    @distributed_trace
    def list_by_resource_group(
        self,
        resource_group_name: str,
        **kwargs: Any
    ) -> AsyncIterable["_models.FactoryListResponse"]:
        """Lists factories.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either FactoryListResponse or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.datafactory.models.FactoryListResponse]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.FactoryListResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    api_version=api_version,
                    template_url=self.list_by_resource_group.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_by_resource_group_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("FactoryListResponse", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response


        return AsyncItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories"}  # type: ignore

    @distributed_trace_async
    async def create_or_update(
        self,
        resource_group_name: str,
        factory_name: str,
        factory: "_models.Factory",
        if_match: Optional[str] = None,
        **kwargs: Any
    ) -> "_models.Factory":
        """Creates or updates a factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param factory: Factory resource definition.
        :type factory: ~azure.mgmt.datafactory.models.Factory
        :param if_match: ETag of the factory entity. Should only be specified for update, for which it
         should match existing entity or can be * for unconditional update. Default value is None.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Factory, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.Factory
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Factory"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(factory, 'Factory')

        request = build_create_or_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            if_match=if_match,
            template_url=self.create_or_update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Factory', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}"}  # type: ignore


    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        factory_name: str,
        factory_update_parameters: "_models.FactoryUpdateParameters",
        **kwargs: Any
    ) -> "_models.Factory":
        """Updates a factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param factory_update_parameters: The parameters for updating a factory.
        :type factory_update_parameters: ~azure.mgmt.datafactory.models.FactoryUpdateParameters
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Factory, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.Factory
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.Factory"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(factory_update_parameters, 'FactoryUpdateParameters')

        request = build_update_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.update.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('Factory', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        factory_name: str,
        if_none_match: Optional[str] = None,
        **kwargs: Any
    ) -> Optional["_models.Factory"]:
        """Gets a factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param if_none_match: ETag of the factory entity. Should only be specified for get. If the ETag
         matches the existing entity tag, or if * was provided, then no content will be returned.
         Default value is None.
        :type if_none_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Factory, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.Factory or None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.Factory"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            api_version=api_version,
            if_none_match=if_none_match,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 304]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Factory', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}"}  # type: ignore


    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self,
        resource_group_name: str,
        factory_name: str,
        **kwargs: Any
    ) -> None:
        """Deletes a factory.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str

        
        request = build_delete_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            api_version=api_version,
            template_url=self.delete.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}"}  # type: ignore


    @distributed_trace_async
    async def get_git_hub_access_token(
        self,
        resource_group_name: str,
        factory_name: str,
        git_hub_access_token_request: "_models.GitHubAccessTokenRequest",
        **kwargs: Any
    ) -> "_models.GitHubAccessTokenResponse":
        """Get GitHub Access Token.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param git_hub_access_token_request: Get GitHub access token request definition.
        :type git_hub_access_token_request: ~azure.mgmt.datafactory.models.GitHubAccessTokenRequest
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GitHubAccessTokenResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.GitHubAccessTokenResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GitHubAccessTokenResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(git_hub_access_token_request, 'GitHubAccessTokenRequest')

        request = build_get_git_hub_access_token_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.get_git_hub_access_token.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GitHubAccessTokenResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_git_hub_access_token.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getGitHubAccessToken"}  # type: ignore


    @distributed_trace_async
    async def get_data_plane_access(
        self,
        resource_group_name: str,
        factory_name: str,
        policy: "_models.UserAccessPolicy",
        **kwargs: Any
    ) -> "_models.AccessPolicyResponse":
        """Get Data Plane access.

        :param resource_group_name: The resource group name.
        :type resource_group_name: str
        :param factory_name: The factory name.
        :type factory_name: str
        :param policy: Data Plane user access policy definition.
        :type policy: ~azure.mgmt.datafactory.models.UserAccessPolicy
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccessPolicyResponse, or the result of cls(response)
        :rtype: ~azure.mgmt.datafactory.models.AccessPolicyResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccessPolicyResponse"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2018-06-01")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(policy, 'UserAccessPolicy')

        request = build_get_data_plane_access_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            factory_name=factory_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.get_data_plane_access.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AccessPolicyResponse', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_data_plane_access.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataFactory/factories/{factoryName}/getDataPlaneAccess"}  # type: ignore

