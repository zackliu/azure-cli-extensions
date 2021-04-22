# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import websocket
import threading
import time
import sys
import json
from knack.util import CLIError
from .vendored_sdks.azure_messaging_webpubsubservice.azure.messaging.webpubsubservice import build_authentication_token
from azure.core.credentials import AzureKeyCredential

def start_client(cmd, client, resource_group_name, webpubsub_name, hub_name):
    keys = client.list_keys(resource_group_name, webpubsub_name)
    resource = client.get(resource_group_name, webpubsub_name)
    key = keys.primary_key
    host = resource.host_name
    token = build_authentication_token('https://' + host, hub_name, key, roles=['webpubsub.sendToGroup', 'webpubsub.joinLeaveGroup'])
    ws = websocket.create_connection(token['url'], subprotocols=['json.webpubsub.azure.v1'])
    ws_client = WebsocketClient(ws)
    ws_client.daemon = True
    ws_client.start()
    publisher = Publisher(ws)
    publisher.daemon = True
    publisher.start()
    while True:
        time.sleep(1)
    ws_client.join()
    publisher.join()


class WebsocketClient(threading.Thread):
    def __init__(self, ws):
        threading.Thread.__init__(self)
        self.ws = ws

    def run(self):
        while True:
            print(self.ws.recv())

    def join(self):
        self.ws.close()
        super().join()


class Publisher(threading.Thread):
    def __init__(self, ws):
        threading.Thread.__init__(self)
        self.ws = ws
        self.id = 0

    def run(self):
        while True:
            input = sys.stdin.readline().strip()
            self._parse(input)

    def join(self):
        super().join()

    def _parse(self, input):
        if input:
            arr = input.split(maxsplit=1)
            if len(arr) != 2:
                print('Invalid input {}'.format(input))
                return

            command = arr[0]
            if command.lower() == 'joingroup':
                group = arr[1]
                payload = json.dumps({
                    'type': 'joinGroup',
                    'group': group,
                    'ackId' : self._get_ack_id()
                })
                self.ws.send(payload)

            elif command.lower() == 'leavegroup':
                group = arr[1]
                payload = json.dumps({
                    'type': 'leaveGroup',
                    'group': group,
                    'ackId' : self._get_ack_id()
                })
                self.ws.send(payload)

            elif command.lower() == 'sendtogroup':
                arr = arr[1].split(maxsplit=1)
                group = arr[0]
                data = arr[1]
                payload = json.dumps({
                    'type': 'sendToGroup',
                    'group': group,
                    'data': data,
                    'ackId' : self._get_ack_id()
                })
                self.ws.send(payload)

            elif command.lower() == 'event':
                arr = arr[1].split(maxsplit=1)
                event = arr[0]
                data = arr[1]
                payload = json.dumps({
                    'type': 'event',
                    'event': event,
                    'data': data
                })
                self.ws.send(payload)

            else:
                print('Invalid input {}'.format(input))

    def _get_ack_id(self):
        self.id = self.id + 1
        return self.id

