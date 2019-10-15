from azure.cli.core.commands import CliCommandType
from azext_concierge.concierge.common.exception_handler import concierge_exception_handler

createops = CliCommandType(
    operations_tmpl='azext_concierge.concierge.general.create#{}',
    exception_handler=concierge_exception_handler
)

def load_general_commands(self, _):
    with self.command_group('concierge', command_type=createops) as g:
        g.command('create', 'create_resources')
