# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_webpubsubdata._client_factory import cf_webpubsubdata


def load_command_table(self, _):

    client_sdk = CliCommandType(
        operations_tmpl='azext_webpubsubdata.client#{}',
        client_factory=cf_webpubsubdata)


    server_sdk = CliCommandType(
        operations_tmpl='azext_webpubsubdata.server#{}',
        client_factory=cf_webpubsubdata)

    with self.command_group('webpubsubdata', client_sdk) as g:
        g.command('show', 'get')

    with self.command_group('webpubsubdata client', client_sdk) as g:
        g.command('listen', 'listen')


    with self.command_group('webpubsubdata service', server_sdk) as g:
        g.command('broadcast', 'broadcast')

