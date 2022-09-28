# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
from urllib.parse import parse_qs, urljoin, urlparse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
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
from ..._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_list_request(
    location: str,
    gallery_unique_name: str,
    gallery_image_name: str,
    subscription_id: str,
    *,
    shared_to: Optional[Union[str, "_models.SharedToValues"]] = None,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-09-30"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/sharedGalleries/{galleryUniqueName}/images/{galleryImageName}/versions",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str"),
        "galleryUniqueName": _SERIALIZER.url("gallery_unique_name", gallery_unique_name, "str"),
        "galleryImageName": _SERIALIZER.url("gallery_image_name", gallery_image_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")
    if shared_to is not None:
        _params["sharedTo"] = _SERIALIZER.query("shared_to", shared_to, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(
    location: str,
    gallery_unique_name: str,
    gallery_image_name: str,
    gallery_image_version_name: str,
    subscription_id: str,
    **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-09-30"))  # type: str
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/sharedGalleries/{galleryUniqueName}/images/{galleryImageName}/versions/{galleryImageVersionName}",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str"),
        "location": _SERIALIZER.url("location", location, "str"),
        "galleryUniqueName": _SERIALIZER.url("gallery_unique_name", gallery_unique_name, "str"),
        "galleryImageName": _SERIALIZER.url("gallery_image_name", gallery_image_name, "str"),
        "galleryImageVersionName": _SERIALIZER.url("gallery_image_version_name", gallery_image_version_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class SharedGalleryImageVersionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2020_09_30.ComputeManagementClient`'s
        :attr:`shared_gallery_image_versions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def list(
        self,
        location: str,
        gallery_unique_name: str,
        gallery_image_name: str,
        shared_to: Optional[Union[str, "_models.SharedToValues"]] = None,
        **kwargs: Any
    ) -> Iterable["_models.SharedGalleryImageVersion"]:
        """List shared gallery image versions by subscription id or tenant id.

        :param location: Resource location. Required.
        :type location: str
        :param gallery_unique_name: The unique name of the Shared Gallery. Required.
        :type gallery_unique_name: str
        :param gallery_image_name: The name of the Shared Gallery Image Definition from which the Image
         Versions are to be listed. Required.
        :type gallery_image_name: str
        :param shared_to: The query parameter to decide what shared galleries to fetch when doing
         listing operations. "tenant" Default value is None.
        :type shared_to: str or ~azure.mgmt.compute.v2020_09_30.models.SharedToValues
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either SharedGalleryImageVersion or the result of
         cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2020_09_30.models.SharedGalleryImageVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-09-30"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SharedGalleryImageVersionList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    location=location,
                    gallery_unique_name=gallery_unique_name,
                    gallery_image_name=gallery_image_name,
                    subscription_id=self._config.subscription_id,
                    shared_to=shared_to,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
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
            deserialized = self._deserialize("SharedGalleryImageVersionList", pipeline_response)
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

    list.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/sharedGalleries/{galleryUniqueName}/images/{galleryImageName}/versions"}  # type: ignore

    @distributed_trace
    def get(
        self,
        location: str,
        gallery_unique_name: str,
        gallery_image_name: str,
        gallery_image_version_name: str,
        **kwargs: Any
    ) -> _models.SharedGalleryImageVersion:
        """Get a shared gallery image version by subscription id or tenant id.

        :param location: Resource location. Required.
        :type location: str
        :param gallery_unique_name: The unique name of the Shared Gallery. Required.
        :type gallery_unique_name: str
        :param gallery_image_name: The name of the Shared Gallery Image Definition from which the Image
         Versions are to be listed. Required.
        :type gallery_image_name: str
        :param gallery_image_version_name: The name of the gallery image version to be created. Needs
         to follow semantic version name pattern: The allowed characters are digit and period. Digits
         must be within the range of a 32-bit integer. Format:
         :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`. Required.
        :type gallery_image_version_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SharedGalleryImageVersion or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2020_09_30.models.SharedGalleryImageVersion
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2020-09-30"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.SharedGalleryImageVersion]

        request = build_get_request(
            location=location,
            gallery_unique_name=gallery_unique_name,
            gallery_image_name=gallery_image_name,
            gallery_image_version_name=gallery_image_version_name,
            subscription_id=self._config.subscription_id,
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

        deserialized = self._deserialize("SharedGalleryImageVersion", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/sharedGalleries/{galleryUniqueName}/images/{galleryImageName}/versions/{galleryImageVersionName}"}  # type: ignore
