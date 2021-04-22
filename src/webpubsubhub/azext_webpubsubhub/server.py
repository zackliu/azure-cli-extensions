# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError
from .vendored_sdks.azure_messaging_webpubsubservice.azure.messaging.webpubsubservice import (
    WebPubSubServiceClient
)
from .vendored_sdks.azure_messaging_webpubsubservice.azure.messaging.webpubsubservice.rest import *

def broadcast(cmd, client, resource_group_name, webpubsub_name, hub_name, payload):    
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_send_to_all_request(hub_name, content=payload, content_type='text/plain'))
    res.raise_for_status()

def check_connection_exists(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_connection_exists_request(hub_name, connection_id))
    return True if res.status_code == 200 else False

def close_connection(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_close_client_connection_request(hub_name, connection_id))
    res.raise_for_status()

def send_connection(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id, payload):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_send_to_connection_request(hub_name, connection_id, content=payload, content_type='text/plain'))
    res.raise_for_status()

def add_connection_to_group(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id, group_name):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_add_connection_to_group_request(hub_name, group_name, connection_id))
    res.raise_for_status()

def remove_connection_from_group(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id, group_name):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_remove_connection_from_group_request(hub_name, group_name, connection_id))
    res.raise_for_status()

def send_group(cmd, client, resource_group_name, webpubsub_name, hub_name, group_name, payload):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_send_to_group_request(hub_name, group_name, content=payload, content_type='text/plain'))
    res.raise_for_status()

def check_user_exists(cmd, client, resource_group_name, webpubsub_name, hub_name, user_id):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_user_exists_request(hub_name, user_id))
    return True if res.status_code == 200 else False

def send_user(cmd, client, resource_group_name, webpubsub_name, hub_name, user_id, payload):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_send_to_user_request(hub_name, user_id, content=payload, content_type='text/plain'))
    res.raise_for_status()

def add_user_to_group(cmd, client, resource_group_name, webpubsub_name, hub_name, user_id, group_name):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_add_user_to_group_request(hub_name, group_name, user_id))
    res.raise_for_status()

def remove_user_from_group(cmd, client, resource_group_name, webpubsub_name, hub_name, user_id, group_name=None):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    if group_name:        
        res = service_client.send_request(build_remove_user_from_group_request(hub_name, group_name, user_id))
    else:
        res = service_client.send_request(build_remove_user_from_all_groups_request(hub_name, user_id))
    res.raise_for_status()

def grant_permission(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id, permission, group_name):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_grant_permission_request(hub_name, permission, connection_id, target_name=group_name))
    res.raise_for_status()

def revoke_permission(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id, permission, group_name):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_revoke_permission_request(hub_name, permission, connection_id, target_name=group_name))
    res.raise_for_status()

def check_permission(cmd, client, resource_group_name, webpubsub_name, hub_name, connection_id, permission, group_name):
    service_client = _get_service_client(client, resource_group_name, webpubsub_name)
    res = service_client.send_request(build_check_permission_request(hub_name, permission, connection_id, target_name=group_name))
    res.raise_for_status()

def _get_service_client(client, resource_group_name, webpubsub_name):
    keys = client.list_keys(resource_group_name, webpubsub_name)
    return WebPubSubServiceClient(keys.primary_connection_string)