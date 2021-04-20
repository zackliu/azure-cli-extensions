# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ACLAction(str, Enum):

    allow = "Allow"
    deny = "Deny"


class UpstreamAuthType(str, Enum):

    none = "None"
    managed_identity = "ManagedIdentity"


class FeatureFlags(str, Enum):

    enable_connectivity_logs = "EnableConnectivityLogs"
    enable_messaging_logs = "EnableMessagingLogs"
    enable_live_trace = "EnableLiveTrace"


class KeyType(str, Enum):

    primary = "Primary"
    secondary = "Secondary"


class ManagedIdentityType(str, Enum):

    none = "None"
    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"


class WebPubSubRequestType(str, Enum):

    client_connection = "ClientConnection"
    server_connection = "ServerConnection"
    restapi = "RESTAPI"
    trace = "Trace"


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"


class ProvisioningState(str, Enum):

    unknown = "Unknown"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    running = "Running"
    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    moving = "Moving"


class PrivateLinkServiceConnectionStatus(str, Enum):

    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
    disconnected = "Disconnected"


class WebPubSubSkuTier(str, Enum):

    free = "Free"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class SharedPrivateLinkResourceStatus(str, Enum):

    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"
    disconnected = "Disconnected"
    timeout = "Timeout"
