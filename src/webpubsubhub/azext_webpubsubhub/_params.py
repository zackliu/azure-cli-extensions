# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# pylint: disable=line-too-long

from knack.arguments import CLIArgumentType


def load_arguments(self, _):

    from azure.cli.core.commands.parameters import tags_type
    from azure.cli.core.commands.validators import get_default_location_from_resource_group

    webpubsubhub_name_type = CLIArgumentType(options_list='--webpubsubhub-name', help='Name of the Webpubsubhub.', id_part='name')

    with self.argument_context('webpubsubhub') as c:
        c.argument('tags', tags_type)
        c.argument('location', validator=get_default_location_from_resource_group)
        c.argument('webpubsub_name', webpubsubhub_name_type, options_list=['--name', '-n'])
        c.argument('hub_name', help='The hub name.')

    for scope in ['webpubsubhub service connection',
                  'webpubsubhub service permission',
                  'webpubsubhub service group add-connection',
                  'webpubsubhub service group remove-connection']:
        with self.argument_context(scope) as c:
            c.argument('connection_id', options_list=['--connection-id', '-c'], help='The client connection id.')

    for scope in ['webpubsubhub service broadcast',
                  'webpubsubhub service connection send',
                  'webpubsubhub service group send',
                  'webpubsubhub service user send']:
        with self.argument_context(scope) as c:
            c.argument('payload', help='The payload to send.')

    for scope in ['webpubsubhub service group',
                  'webpubsubhub service permission']:
        with self.argument_context(scope) as c:
            c.argument('group_name', help='The group name.')
    
    for scope in ['webpubsubhub service user', 'webpubsubhub service group add-user', 'webpubsubhub service group remove-user']:
        with self.argument_context(scope) as c:
            c.argument('user_id', help='The user id.')

    with self.argument_context('webpubsubhub service permission') as c:
            c.argument('permission', help='The permission.')