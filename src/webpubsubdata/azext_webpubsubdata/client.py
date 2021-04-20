# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import websocket
import threading
import time
from knack.util import CLIError
from .vendored_sdks.azure_messaging_webpubsubservice.azure.messaging.webpubsubservice import build_authentication_token
from azure.core.credentials import AzureKeyCredential

def listen(cmd, client, resource_group_name, webpubsub_name, hub_name):
    keys = client.list_keys(resource_group_name, webpubsub_name)
    resource = client.get(resource_group_name, webpubsub_name)
    key = keys.primary_key
    host = resource.host_name
    token = build_authentication_token('https://' + host, hub_name, key)
    print(token)
    ws = websocket.create_connection(token['url'], subprotocols=['json.webpubsub.azure.v1'])
    f = MyThread(ws)
    f.start()
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        f.join()
    ws.close()
    

def get(cmd, client, resource_group_name, webpubsubdata_name, location=None, tags=None):
    return client.get('chenylwps', 'chenylwpscli1')


class MyThread(threading.Thread):
    die = False
    def __init__(self, ws):
        threading.Thread.__init__(self)
        self.ws = ws

    def run (self):
        while not self.die:
            print('pre')
            print(self.ws.recv())
            print('post')

    def join(self):
        self.die = True
        super().join()