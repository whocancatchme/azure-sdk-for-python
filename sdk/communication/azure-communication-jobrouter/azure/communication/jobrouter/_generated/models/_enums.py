# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class JobStateSelector(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """JobStateSelector."""

    ALL = "all"
    PENDING_CLASSIFICATION = "pendingClassification"
    QUEUED = "queued"
    ASSIGNED = "assigned"
    COMPLETED = "completed"
    CLOSED = "closed"
    CANCELLED = "cancelled"
    CLASSIFICATION_FAILED = "classificationFailed"
    ACTIVE = "active"


class LabelOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Describes how the value of the label is compared to the value pass through."""

    EQUAL = "equal"
    NOT_EQUAL = "notEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_EQUAL = "lessThanEqual"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_EQUAL = "greaterThanEqual"


class RouterJobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the Job."""

    PENDING_CLASSIFICATION = "pendingClassification"
    QUEUED = "queued"
    ASSIGNED = "assigned"
    COMPLETED = "completed"
    CLOSED = "closed"
    CANCELLED = "cancelled"
    CLASSIFICATION_FAILED = "classificationFailed"
    CREATED = "created"


class RouterWorkerState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The current state of the worker."""

    ACTIVE = "active"
    DRAINING = "draining"
    INACTIVE = "inactive"


class ScoringRuleParameterSelector(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Supported parameters for scoring workers."""

    JOB_LABELS = "jobLabels"
    WORKER_SELECTORS = "workerSelectors"


class WorkerSelectorState(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The state of the worker selector."""

    ACTIVE = "active"
    EXPIRED = "expired"


class WorkerStateSelector(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """WorkerStateSelector."""

    ACTIVE = "active"
    DRAINING = "draining"
    INACTIVE = "inactive"
    ALL = "all"
