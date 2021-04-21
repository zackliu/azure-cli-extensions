# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import websocket
import threading
import time
import sys
from knack.util import CLIError
from .vendored_sdks.azure_messaging_webpubsubservice.azure.messaging.webpubsubservice import build_authentication_token
from azure.core.credentials import AzureKeyCredential

def start_client(cmd, client, resource_group_name, webpubsub_name, hub_name):
    keys = client.list_keys(resource_group_name, webpubsub_name)
    resource = client.get(resource_group_name, webpubsub_name)
    key = keys.primary_key
    host = resource.host_name
    token = build_authentication_token('https://' + host, hub_name, key)
    t = WebsocketClient(token['url'])
    t.daemon = True
    t.start()
    while True:
        time.sleep(1)
    t.join()
    

def get(cmd, client, resource_group_name, webpubsubhub_name, location=None, tags=None):
    return client.get('chenylwps', 'chenylwpscli1')


class WebsocketClient(threading.Thread):
    die = False
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.ws = websocket.create_connection(url, subprotocols=['json.webpubsub.azure.v1'])

    def run (self):
        while True:
            print(self.ws.recv())

    def join(self):
        self.die = True
        self.ws.close()
        super().join()
