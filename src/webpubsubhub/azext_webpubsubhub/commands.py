# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_webpubsubhub._client_factory import cf_webpubsubhub


def load_command_table(self, _):

    client_sdk = CliCommandType(
        operations_tmpl='azext_webpubsubhub.client#{}',
        client_factory=cf_webpubsubhub)


    server_sdk = CliCommandType(
        operations_tmpl='azext_webpubsubhub.server#{}',
        client_factory=cf_webpubsubhub)


    with self.command_group('webpubsubhub', client_sdk) as g:
        g.command('start-client', 'start_client')


    with self.command_group('webpubsubhub service', server_sdk) as g:
        g.command('broadcast', 'broadcast')


    with self.command_group('webpubsubhub service connection', server_sdk) as g:
        g.command('exist', 'check_connection_exists')
        g.command('close', 'close_connection')
        g.command('send', 'send_connection')


    with self.command_group('webpubsubhub service group', server_sdk) as g:
        g.command('add-connection', 'add_connection_to_group')
        g.command('remove-connection', 'remove_connection_from_group')
        g.command('send', 'send_group')
        g.command('add-user', 'add_user_to_group')
        g.command('remove-user', 'remove_user_from_group')


    with self.command_group('webpubsubhub service user', server_sdk) as g:
        g.command('send', 'send_user')
        g.command('exist', 'check_user_exists')

    
    with self.command_group('webpubsubhub service permission', server_sdk) as g:
        g.command('grant', 'grant_permission')
        g.command('revoke', 'revoke_permission')
        g.command('check', 'check_permission')

        


