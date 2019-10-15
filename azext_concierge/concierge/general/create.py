from knack.log import get_logger
from knack.util import CLIError

from azext_concierge.concierge.common.shell import execute_shell_process

logger = get_logger(__name__)

FUNCTION_TEMPLATE_URI = (
    "https://dev.azure.com/eg-internal/Concierge_AzureFunctionCSharp/"
    "_apis/git/repositories/Concierge_AzureFunctionCSharp/items"
    "?path=%2FARM%20templates%2Ffunction_and_storage_account.json"
)

def create_resources(organization, project, location, group_name,
    site_type, site_name):
    print('Ready to create resources!')

    if organization is None:
        raise CLIError('An organization parameter must be provided via --organization or --org.')

    if project is None:
        raise CLIError('A project name parameter must be provided via --project or -p.')

    if location is None:
        raise CLIError('A location parameter must be provided via --location or -l.')

    if group_name is None:
        raise CLIError('A group-name parameter must be provided via --group-name or -g.')

    if site_type is None:
        raise CLIError('A site-type parameter must be provided via --site-type or -t.')

    if site_name is None:
        raise CLIError('A site-name parameter must be provided via --site-name or -s.')

    create_azure_devops_project(organization, project)
    create_azure_resource_group(location, group_name)
    create_azure_resources(group_name, site_type, site_name)

# az devops project create --name {ado_project_name} --organization https://dev.azure.com/{ado_project_organization}
def create_azure_devops_project(organization, project):
    message = 'Creating the Azure DevOps project...'

    cmd = ['az', 'devops', 'project', 'create', '--name', project,
        '--organization', 'https://dev.azure.com/{}'.format(organization)]

    execute_shell_process(message, cmd)

# az group create -l {resource_group_location} -n {resource_group_name}
def create_azure_resource_group(location, group_name):
    message = 'Creating the Azure resource group...'

    cmd = ['az', 'group', 'create', '-l', location, '-n', group_name]

    execute_shell_process(message, cmd)

# az group deployment create -g {resource-group-name} --template-uri {path-to-template}
def create_azure_resources(group_name, site_type, site_name):
    message = 'Creating Azure resources in resource group {}...'.format(group_name)

    cmd = ['az', 'group', 'deployment', 'create', '-g', group_name,
        '--parameters', 'appName={}'.format(site_name), '--template-uri', FUNCTION_TEMPLATE_URI]

    execute_shell_process(message, cmd)
