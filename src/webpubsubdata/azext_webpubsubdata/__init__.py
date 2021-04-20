# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.core import AzCommandsLoader

from azext_webpubsubdata._help import helps  # pylint: disable=unused-import


class WebpubsubdataCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azext_webpubsubdata._client_factory import cf_webpubsubdata
        webpubsubdata_custom = CliCommandType(
            operations_tmpl='azext_webpubsubdata.custom#{}',
            client_factory=cf_webpubsubdata)
        super(WebpubsubdataCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                  custom_command_type=webpubsubdata_custom)

    def load_command_table(self, args):
        from azext_webpubsubdata.commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_webpubsubdata._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = WebpubsubdataCommandsLoader
