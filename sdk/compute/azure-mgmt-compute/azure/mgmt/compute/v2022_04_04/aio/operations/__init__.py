# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._cloud_service_role_instances_operations import CloudServiceRoleInstancesOperations
from ._cloud_service_roles_operations import CloudServiceRolesOperations
from ._cloud_services_operations import CloudServicesOperations
from ._cloud_services_update_domain_operations import CloudServicesUpdateDomainOperations
from ._cloud_service_operating_systems_operations import CloudServiceOperatingSystemsOperations

from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CloudServiceRoleInstancesOperations",
    "CloudServiceRolesOperations",
    "CloudServicesOperations",
    "CloudServicesUpdateDomainOperations",
    "CloudServiceOperatingSystemsOperations",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
