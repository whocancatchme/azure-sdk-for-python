# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, cast, overload

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
from azure.core.polling import AsyncLROPoller, AsyncNoPolling, AsyncPollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.async_arm_polling import AsyncARMPolling

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._virtual_machine_scale_set_vm_extensions_operations import (
    build_create_or_update_request,
    build_delete_request,
    build_get_request,
    build_list_request,
    build_update_request,
)

T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class VirtualMachineScaleSetVMExtensionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.compute.v2019_12_01.aio.ComputeManagementClient`'s
        :attr:`virtual_machine_scale_set_vm_extensions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    async def _create_or_update_initial(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: Union[_models.VirtualMachineExtension, IO],
        **kwargs: Any
    ) -> _models.VirtualMachineExtension:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtension]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(extension_parameters, (IO, bytes)):
            _content = extension_parameters
        else:
            _json = self._serialize.body(extension_parameters, "VirtualMachineExtension")

        request = build_create_or_update_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            instance_id=instance_id,
            vm_extension_name=vm_extension_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._create_or_update_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize("VirtualMachineExtension", pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize("VirtualMachineExtension", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _create_or_update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: _models.VirtualMachineExtension,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VirtualMachineExtension]:
        """The operation to create or update the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param extension_parameters: Parameters supplied to the Create Virtual Machine Extension
         operation. Required.
        :type extension_parameters: ~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineExtension or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VirtualMachineExtension]:
        """The operation to create or update the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param extension_parameters: Parameters supplied to the Create Virtual Machine Extension
         operation. Required.
        :type extension_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineExtension or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_create_or_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: Union[_models.VirtualMachineExtension, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VirtualMachineExtension]:
        """The operation to create or update the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param extension_parameters: Parameters supplied to the Create Virtual Machine Extension
         operation. Is either a model type or a IO type. Required.
        :type extension_parameters: ~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension or
         IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineExtension or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtension]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._create_or_update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                instance_id=instance_id,
                vm_extension_name=vm_extension_name,
                extension_parameters=extension_parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("VirtualMachineExtension", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    async def _update_initial(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: Union[_models.VirtualMachineExtensionUpdate, IO],
        **kwargs: Any
    ) -> _models.VirtualMachineExtension:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtension]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(extension_parameters, (IO, bytes)):
            _content = extension_parameters
        else:
            _json = self._serialize.body(extension_parameters, "VirtualMachineExtensionUpdate")

        request = build_update_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            instance_id=instance_id,
            vm_extension_name=vm_extension_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self._update_initial.metadata["url"],
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

        deserialized = self._deserialize("VirtualMachineExtension", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    _update_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: _models.VirtualMachineExtensionUpdate,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VirtualMachineExtension]:
        """The operation to update the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param extension_parameters: Parameters supplied to the Update Virtual Machine Extension
         operation. Required.
        :type extension_parameters:
         ~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtensionUpdate
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineExtension or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def begin_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VirtualMachineExtension]:
        """The operation to update the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param extension_parameters: Parameters supplied to the Update Virtual Machine Extension
         operation. Required.
        :type extension_parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineExtension or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def begin_update(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        extension_parameters: Union[_models.VirtualMachineExtensionUpdate, IO],
        **kwargs: Any
    ) -> AsyncLROPoller[_models.VirtualMachineExtension]:
        """The operation to update the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param extension_parameters: Parameters supplied to the Update Virtual Machine Extension
         operation. Is either a model type or a IO type. Required.
        :type extension_parameters:
         ~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtensionUpdate or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either VirtualMachineExtension or the
         result of cls(response)
        :rtype:
         ~azure.core.polling.AsyncLROPoller[~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtension]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._update_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                instance_id=instance_id,
                vm_extension_name=vm_extension_name,
                extension_parameters=extension_parameters,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize("VirtualMachineExtension", pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_update.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    async def _delete_initial(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, vm_scale_set_name: str, instance_id: str, vm_extension_name: str, **kwargs: Any
    ) -> None:
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]

        request = build_delete_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            instance_id=instance_id,
            vm_extension_name=vm_extension_name,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self._delete_initial.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)  # type: ignore

        pipeline_response = await self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    @distributed_trace_async
    async def begin_delete(
        self, resource_group_name: str, vm_scale_set_name: str, instance_id: str, vm_extension_name: str, **kwargs: Any
    ) -> AsyncLROPoller[None]:
        """The operation to delete the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be AsyncARMPolling. Pass in False for
         this operation to not poll, or pass in your own initialized polling object for a personal
         polling strategy.
        :paramtype polling: bool or ~azure.core.polling.AsyncPollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of AsyncLROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.AsyncLROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[None]
        polling = kwargs.pop("polling", True)  # type: Union[bool, AsyncPollingMethod]
        lro_delay = kwargs.pop("polling_interval", self._config.polling_interval)
        cont_token = kwargs.pop("continuation_token", None)  # type: Optional[str]
        if cont_token is None:
            raw_result = await self._delete_initial(  # type: ignore
                resource_group_name=resource_group_name,
                vm_scale_set_name=vm_scale_set_name,
                instance_id=instance_id,
                vm_extension_name=vm_extension_name,
                api_version=api_version,
                cls=lambda x, y, z: x,
                headers=_headers,
                params=_params,
                **kwargs
            )
        kwargs.pop("error_map", None)

        def get_long_running_output(pipeline_response):  # pylint: disable=inconsistent-return-statements
            if cls:
                return cls(pipeline_response, None, {})

        if polling is True:
            polling_method = cast(AsyncPollingMethod, AsyncARMPolling(lro_delay, **kwargs))  # type: AsyncPollingMethod
        elif polling is False:
            polling_method = cast(AsyncPollingMethod, AsyncNoPolling())
        else:
            polling_method = polling
        if cont_token:
            return AsyncLROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output,
            )
        return AsyncLROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_delete.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        vm_extension_name: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.VirtualMachineExtension:
        """The operation to get the VMSS VM extension.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param vm_extension_name: The name of the virtual machine extension. Required.
        :type vm_extension_name: str
        :param expand: The expand expression to apply on the operation. Default value is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineExtension or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtension
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtension]

        request = build_get_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            instance_id=instance_id,
            vm_extension_name=vm_extension_name,
            subscription_id=self._config.subscription_id,
            expand=expand,
            api_version=api_version,
            template_url=self.get.metadata["url"],
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

        deserialized = self._deserialize("VirtualMachineExtension", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}"}  # type: ignore

    @distributed_trace_async
    async def list(
        self,
        resource_group_name: str,
        vm_scale_set_name: str,
        instance_id: str,
        expand: Optional[str] = None,
        **kwargs: Any
    ) -> _models.VirtualMachineExtensionsListResult:
        """The operation to get all extensions of an instance in Virtual Machine Scaleset.

        :param resource_group_name: The name of the resource group. Required.
        :type resource_group_name: str
        :param vm_scale_set_name: The name of the VM scale set. Required.
        :type vm_scale_set_name: str
        :param instance_id: The instance ID of the virtual machine. Required.
        :type instance_id: str
        :param expand: The expand expression to apply on the operation. Default value is None.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: VirtualMachineExtensionsListResult or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_12_01.models.VirtualMachineExtensionsListResult
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "2019-12-01"))  # type: str
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.VirtualMachineExtensionsListResult]

        request = build_list_request(
            resource_group_name=resource_group_name,
            vm_scale_set_name=vm_scale_set_name,
            instance_id=instance_id,
            subscription_id=self._config.subscription_id,
            expand=expand,
            api_version=api_version,
            template_url=self.list.metadata["url"],
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

        deserialized = self._deserialize("VirtualMachineExtensionsListResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions"}  # type: ignore
