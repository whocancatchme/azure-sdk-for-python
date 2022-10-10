# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class AlertSeverity(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The risk level of the threat that was detected. Learn more:
    https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified.
    """

    #: Informational
    INFORMATIONAL = "Informational"
    #: Low
    LOW = "Low"
    #: Medium
    MEDIUM = "Medium"
    #: High
    HIGH = "High"


class AlertStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The life cycle status of the alert."""

    #: An alert which doesn't specify a value is assigned the status 'Active'
    ACTIVE = "Active"
    #: An alert which is in handling state
    IN_PROGRESS = "InProgress"
    #: Alert closed after handling
    RESOLVED = "Resolved"
    #: Alert dismissed as false positive
    DISMISSED = "Dismissed"


class BundleType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Alert Simulator supported bundles."""

    APP_SERVICES = "AppServices"
    DNS = "DNS"
    KEY_VAULTS = "KeyVaults"
    KUBERNETES_SERVICE = "KubernetesService"
    RESOURCE_MANAGER = "ResourceManager"
    SQL_SERVERS = "SqlServers"
    STORAGE_ACCOUNTS = "StorageAccounts"
    VIRTUAL_MACHINES = "VirtualMachines"
    COSMOS_DBS = "CosmosDbs"


class Intent(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kill chain related intent behind the alert. For list of supported values, and explanations
    of Azure Security Center's supported kill chain intents.
    """

    #: Unknown
    UNKNOWN = "Unknown"
    #: PreAttack could be either an attempt to access a certain resource regardless of a malicious
    #: intent, or a failed attempt to gain access to a target system to gather information prior to
    #: exploitation. This step is usually detected as an attempt, originating from outside the
    #: network, to scan the target system and find a way in.  Further details on the PreAttack stage
    #: can be read in `MITRE Pre-Att&ck matrix <https://attack.mitre.org/matrices/pre/>`_.
    PRE_ATTACK = "PreAttack"
    #: InitialAccess is the stage where an attacker manages to get foothold on the attacked resource.
    INITIAL_ACCESS = "InitialAccess"
    #: Persistence is any access, action, or configuration change to a system that gives a threat
    #: actor a persistent presence on that system.
    PERSISTENCE = "Persistence"
    #: Privilege escalation is the result of actions that allow an adversary to obtain a higher level
    #: of permissions on a system or network.
    PRIVILEGE_ESCALATION = "PrivilegeEscalation"
    #: Defense evasion consists of techniques an adversary may use to evade detection or avoid other
    #: defenses.
    DEFENSE_EVASION = "DefenseEvasion"
    #: Credential access represents techniques resulting in access to or control over system, domain,
    #: or service credentials that are used within an enterprise environment.
    CREDENTIAL_ACCESS = "CredentialAccess"
    #: Discovery consists of techniques that allow the adversary to gain knowledge about the system
    #: and internal network.
    DISCOVERY = "Discovery"
    #: Lateral movement consists of techniques that enable an adversary to access and control remote
    #: systems on a network and could, but does not necessarily, include execution of tools on remote
    #: systems.
    LATERAL_MOVEMENT = "LateralMovement"
    #: The execution tactic represents techniques that result in execution of adversary-controlled
    #: code on a local or remote system.
    EXECUTION = "Execution"
    #: Collection consists of techniques used to identify and gather information, such as sensitive
    #: files, from a target network prior to exfiltration.
    COLLECTION = "Collection"
    #: Exfiltration refers to techniques and attributes that result or aid in the adversary removing
    #: files and information from a target network.
    EXFILTRATION = "Exfiltration"
    #: The command and control tactic represents how adversaries communicate with systems under their
    #: control within a target network.
    COMMAND_AND_CONTROL = "CommandAndControl"
    #: Impact events primarily try to directly reduce the availability or integrity of a system,
    #: service, or network; including manipulation of data to impact a business or operational
    #: process.
    IMPACT = "Impact"
    #: Probing could be either an attempt to access a certain resource regardless of a malicious
    #: intent, or a failed attempt to gain access to a target system to gather information prior to
    #: exploitation.
    PROBING = "Probing"
    #: Exploitation is the stage where an attacker manages to get a foothold on the attacked resource.
    #: This stage is relevant for compute hosts and resources such as user accounts, certificates etc.
    EXPLOITATION = "Exploitation"


class KindEnum(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """The kind of alert simulation."""

    #: Simulate alerts according to bundles
    BUNDLES = "Bundles"


class ResourceIdentifierType(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """There can be multiple identifiers of different type per alert, this field specify the
    identifier type.
    """

    AZURE_RESOURCE = "AzureResource"
    LOG_ANALYTICS = "LogAnalytics"
