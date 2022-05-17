# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, List, Optional, TypeVar

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._vendor import _convert_request, _format_url_section
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False

def build_get_request(
    location: str,
    edge_zone: str,
    publisher_name: str,
    offer: str,
    skus: str,
    version: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "location": _SERIALIZER.url("location", location, 'str'),
        "edgeZone": _SERIALIZER.url("edge_zone", edge_zone, 'str'),
        "publisherName": _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        "offer": _SERIALIZER.url("offer", offer, 'str'),
        "skus": _SERIALIZER.url("skus", skus, 'str'),
        "version": _SERIALIZER.url("version", version, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_request(
    location: str,
    edge_zone: str,
    publisher_name: str,
    offer: str,
    skus: str,
    subscription_id: str,
    *,
    expand: Optional[str] = None,
    top: Optional[int] = None,
    orderby: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions")  # pylint: disable=line-too-long
    path_format_arguments = {
        "location": _SERIALIZER.url("location", location, 'str'),
        "edgeZone": _SERIALIZER.url("edge_zone", edge_zone, 'str'),
        "publisherName": _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        "offer": _SERIALIZER.url("offer", offer, 'str'),
        "skus": _SERIALIZER.url("skus", skus, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if expand is not None:
        _query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')
    if top is not None:
        _query_parameters['$top'] = _SERIALIZER.query("top", top, 'int')
    if orderby is not None:
        _query_parameters['$orderby'] = _SERIALIZER.query("orderby", orderby, 'str')
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_offers_request(
    location: str,
    edge_zone: str,
    publisher_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers")  # pylint: disable=line-too-long
    path_format_arguments = {
        "location": _SERIALIZER.url("location", location, 'str'),
        "edgeZone": _SERIALIZER.url("edge_zone", edge_zone, 'str'),
        "publisherName": _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_publishers_request(
    location: str,
    edge_zone: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers")  # pylint: disable=line-too-long
    path_format_arguments = {
        "location": _SERIALIZER.url("location", location, 'str'),
        "edgeZone": _SERIALIZER.url("edge_zone", edge_zone, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_skus_request(
    location: str,
    edge_zone: str,
    publisher_name: str,
    offer: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus")  # pylint: disable=line-too-long
    path_format_arguments = {
        "location": _SERIALIZER.url("location", location, 'str'),
        "edgeZone": _SERIALIZER.url("edge_zone", edge_zone, 'str'),
        "publisherName": _SERIALIZER.url("publisher_name", publisher_name, 'str'),
        "offer": _SERIALIZER.url("offer", offer, 'str'),
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

class VirtualMachineImagesEdgeZoneOperations(object):
    """VirtualMachineImagesEdgeZoneOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2021_11_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def get(
        self,
        location: str,
        edge_zone: str,
        publisher_name: str,
        offer: str,
        skus: str,
        version: str,
        **kwargs: Any
    ) -> "_models.VirtualMachineImage":
        """Gets a virtual machine image in an edge zone.

        :param location: The name of a supported Azure region.
        :type location: str
        :param edge_zone: The name of the edge zone.
        :type edge_zone: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :param skus: A valid image SKU.
        :type skus: str
        :param version: A valid image SKU version.
        :type version: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineImage, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2021_11_01.models.VirtualMachineImage
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.VirtualMachineImage"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

        
        request = build_get_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            version=version,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('VirtualMachineImage', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}"}  # type: ignore


    @distributed_trace
    def list(
        self,
        location: str,
        edge_zone: str,
        publisher_name: str,
        offer: str,
        skus: str,
        expand: Optional[str] = None,
        top: Optional[int] = None,
        orderby: Optional[str] = None,
        **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of all virtual machine image versions for the specified location, edge zone,
        publisher, offer, and SKU.

        :param location: The name of a supported Azure region.
        :type location: str
        :param edge_zone: The name of the edge zone.
        :type edge_zone: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :param skus: A valid image SKU.
        :type skus: str
        :param expand: The expand expression to apply on the operation. Default value is None.
        :type expand: str
        :param top: An integer value specifying the number of images to return that matches supplied
         values. Default value is None.
        :type top: int
        :param orderby: Specifies the order of the results returned. Formatted as an OData query.
         Default value is None.
        :type orderby: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_11_01.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

        
        request = build_list_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            offer=offer,
            skus=skus,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            expand=expand,
            top=top,
            orderby=orderby,
            template_url=self.list.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[VirtualMachineImageResource]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions"}  # type: ignore


    @distributed_trace
    def list_offers(
        self,
        location: str,
        edge_zone: str,
        publisher_name: str,
        **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of virtual machine image offers for the specified location, edge zone and
        publisher.

        :param location: The name of a supported Azure region.
        :type location: str
        :param edge_zone: The name of the edge zone.
        :type edge_zone: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_11_01.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

        
        request = build_list_offers_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_offers.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[VirtualMachineImageResource]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_offers.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers"}  # type: ignore


    @distributed_trace
    def list_publishers(
        self,
        location: str,
        edge_zone: str,
        **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of virtual machine image publishers for the specified Azure location and edge zone.

        :param location: The name of a supported Azure region.
        :type location: str
        :param edge_zone: The name of the edge zone.
        :type edge_zone: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_11_01.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

        
        request = build_list_publishers_request(
            location=location,
            edge_zone=edge_zone,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_publishers.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[VirtualMachineImageResource]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_publishers.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers"}  # type: ignore


    @distributed_trace
    def list_skus(
        self,
        location: str,
        edge_zone: str,
        publisher_name: str,
        offer: str,
        **kwargs: Any
    ) -> List["_models.VirtualMachineImageResource"]:
        """Gets a list of virtual machine image SKUs for the specified location, edge zone, publisher, and
        offer.

        :param location: The name of a supported Azure region.
        :type location: str
        :param edge_zone: The name of the edge zone.
        :type edge_zone: str
        :param publisher_name: A valid image publisher.
        :type publisher_name: str
        :param offer: A valid image publisher offer.
        :type offer: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of VirtualMachineImageResource, or the result of cls(response)
        :rtype: list[~azure.mgmt.compute.v2021_11_01.models.VirtualMachineImageResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["_models.VirtualMachineImageResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2021-11-01")  # type: str

        
        request = build_list_skus_request(
            location=location,
            edge_zone=edge_zone,
            publisher_name=publisher_name,
            offer=offer,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.list_skus.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[VirtualMachineImageResource]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_skus.metadata = {'url': "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus"}  # type: ignore

