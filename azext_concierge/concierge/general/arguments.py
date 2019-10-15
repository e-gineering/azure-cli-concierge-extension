from knack.arguments import enum_choice_list

_SITE_TYPE_VALUES = ['webapp', 'function']

def load_general_arguments(self, _):
    with self.argument_context('concierge create') as context:
        context.argument('organization', options_list=('--organization', '--org'),
                    help='Azure DevOps organization. Example: MyOrganizationName from https://dev.azure.com/MyOrganizationName/')
        context.argument('project', options_list=('--project', '-p'),
                    help='Name of the project to create in Azure DevOps.')
        context.argument('location', options_list=('--location', '-l'),
                    help='Region in which to create the Azure Resource Group.')
        context.argument('group_name', options_list=('--group-name', '-g'),
                    help='Name of the Azure Resource Group.')
        context.argument('site_type', options_list=('--site-type', '-t'),
                    help='Type of site to create in Azure. You can select webapp or Azure Function currently.',
                    **enum_choice_list(_SITE_TYPE_VALUES))
        context.argument('site_name', options_list=('--site-name', '-s'),
                    help='Name of the Azure webapp or Azure Function.')
