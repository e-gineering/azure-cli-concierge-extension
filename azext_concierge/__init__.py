from knack.help_files import helps

from azure.cli.core import AzCommandsLoader

class ConciergeCommandsLoader(AzCommandsLoader):

    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        custom_type = CliCommandType(operations_tmpl='azext_concierge#{}')
        super(ConciergeCommandsLoader, self).__init__(cli_ctx=cli_ctx,
                                                       custom_command_type=custom_type)

    def load_command_table(self, args):
        from azext_concierge.concierge.general.commands import load_general_commands
        load_general_commands(self, args)
        return self.command_table

    def load_arguments(self, command):
        from azext_concierge.concierge.general.arguments import load_general_arguments
        load_general_arguments(self, command)


COMMAND_LOADER_CLS = ConciergeCommandsLoader
