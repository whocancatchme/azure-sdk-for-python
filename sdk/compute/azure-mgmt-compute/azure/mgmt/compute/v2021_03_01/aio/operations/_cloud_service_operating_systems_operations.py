# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, AsyncIterable, Callable, Dict, Optional, TypeVar
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._cloud_service_operating_systems_operations import (
    build_get_os_family_request,
    build_get_os_version_request,
    build_list_os_families_request,
    build_list_os_versions_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class CloudServiceOperatingSystemsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2021_03_01.aio.ComputeManagementClient`'s
        :attr:`cloud_service_operating_systems` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get_os_version(self, location: str, os_version_name: str, **kwargs: Any) -> _models.OSVersion:
        """Gets properties of a guest operating system version that can be specified in the XML service
        configuration (.cscfg) for a cloud service.

        :param location: Name of the location that the OS version pertains to. Required.
        :type location: str
        :param os_version_name: Name of the OS version. Required.
        :type os_version_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OSVersion or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_03_01.models.OSVersion
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.OSVersion]

        request = build_get_os_version_request(
            location=location,
            os_version_name=os_version_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_os_version.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("OSVersion", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_os_version.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/cloudServiceOsVersions/{osVersionName}"}  # type: ignore

    @distributed_trace
    def list_os_versions(self, location: str, **kwargs: Any) -> AsyncIterable["_models.OSVersion"]:
        """Gets a list of all guest operating system versions available to be specified in the XML service
        configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the
        next page of OS versions. Do this till nextLink is null to fetch all the OS versions.

        :param location: Name of the location that the OS versions pertain to. Required.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OSVersion or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2021_03_01.models.OSVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.OSVersionListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_os_versions_request(
                    location=location,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_os_versions.metadata["url"],
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("OSVersionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_os_versions.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/cloudServiceOsVersions"}  # type: ignore

    @distributed_trace_async
    async def get_os_family(self, location: str, os_family_name: str, **kwargs: Any) -> _models.OSFamily:
        """Gets properties of a guest operating system family that can be specified in the XML service
        configuration (.cscfg) for a cloud service.

        :param location: Name of the location that the OS family pertains to. Required.
        :type location: str
        :param os_family_name: Name of the OS family. Required.
        :type os_family_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: OSFamily or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_03_01.models.OSFamily
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.OSFamily]

        request = build_get_os_family_request(
            location=location,
            os_family_name=os_family_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get_os_family.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize("OSFamily", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_os_family.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/cloudServiceOsFamilies/{osFamilyName}"}  # type: ignore

    @distributed_trace
    def list_os_families(self, location: str, **kwargs: Any) -> AsyncIterable["_models.OSFamily"]:
        """Gets a list of all guest operating system families available to be specified in the XML service
        configuration (.cscfg) for a cloud service. Use nextLink property in the response to get the
        next page of OS Families. Do this till nextLink is null to fetch all the OS Families.

        :param location: Name of the location that the OS families pertain to. Required.
        :type location: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either OSFamily or the result of cls(response)
        :rtype:
         ~azure.core.async_paging.AsyncItemPaged[~azure.mgmt.compute.v2021_03_01.models.OSFamily]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2021-03-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.OSFamilyListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_os_families_request(
                    location=location,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    template_url=self.list_os_families.metadata["url"],
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

        async def extract_data(pipeline_response):
            deserialized = self._deserialize("OSFamilyListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(get_next, extract_data)

    list_os_families.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/cloudServiceOsFamilies"}  # type: ignore
