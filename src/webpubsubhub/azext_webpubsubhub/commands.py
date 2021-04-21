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

