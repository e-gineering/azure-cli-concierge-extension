# Azure CLI Concierge Extension

[![Build status](https://dev.azure.com/eg-internal/Concierge/_apis/build/status/Azure%20CLI%20Concierge)](https://dev.azure.com/eg-internal/Concierge/_build/latest?definitionId=12)

The Azure Concierge Extension for Azure CLI adds a Concierge command to allow easy creation of an Azure DevOps project and associated Azure resources.

This is similar to and inspired by the Azure DevOps Demo Generator, seen [here](https://azuredevopsdemogenerator.azurewebsites.net).

## Usage

```
$ az concierge [group]
```

```
$ az concierge -h

Group
  az concierge : Create a sample Azure DevOps project and Azure resources in a single command.

Commands:
  create : Create resources
```

## Example Usage
```
$ az concierge create \
    --organization MyAzureDevOpsOrganization \
    --project AzureDevOpsProjectName \
    --location 'northcentralus' \
    --group-name ResourceGroupName \
    --site-type function \
    --site-name AzureResourceName
```

By default the template used creates an Azure Function webapp with associated storage account and app service plan all in the same resource group. More types are coming soon.