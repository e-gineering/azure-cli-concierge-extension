from knack.help_files import helps

def load_create_help():
    helps['concierge'] = """
    type: group
    short-summary: Create a new Azure DevOps project and associated Azure resources
    """

    helps['concierge create'] = """
    type: command
    short-summary: Create a new Azure DevOps project and associated Azure resources
    """
