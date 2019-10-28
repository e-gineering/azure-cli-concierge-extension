function PrintLogo {
  Write-Host '                          hN+'
  Write-Host '                      `:+/+ymhso/-`'
  Write-Host '                   -sho:odNNNNNNNNNh+.'
  Write-Host '                 :dm/ /mNNNNNNNNNNNNNNy.'
  Write-Host '               `yNy` oNNNNNNNNNNNNNNNNNN+'
  Write-Host '              `dNh  :NNNNNNNNNNNNNNNNNNNNs'
  Write-Host '              yNN`  yNNNNNNNNNNNNNNNNNNNNN:'
  Write-Host '             `hh+   yhhhhhhhhhhhhhhhhhhhhhs'
  Write-Host '           ``-oo+///oooooooooooooooooooooo+```'
  Write-Host '           osssssssssyysssssssssssssssssssssss/'
  Write-Host '                     smmho/:-oo:.`:ohmNNmds-  -///       ////'
  Write-Host '                       ./ohmhhhdNNNNNNNNNNNNm+sNNN       NNNm'
  Write-Host '                            `:+sssssdddddNNNNosNNN       NNNm'
  Write-Host '                                         `:+y+sNNN       NNNm'
  Write-Host '                                              sNNN       NNNm'
  Write-Host '                                              sNNN       NNNm'
  Write-Host '                                              sNNN       NNNm'
  Write-Host '                                                .N'
  Write-Host '                                                `N'
  Write-Host '                                                `N'
  Write-Host '                                                `N'
  Write-Host
  Write-Host
  Write-Host '********************** Azure Concierge **********************'
  Write-Host
  Write-Host
}

function Show-Menu {
  param (
    [Parameter(Mandatory = $true)]
    [string]$title,
    [Parameter(Mandatory = $true)]
    [System.Object]$options
  )

  Write-Host "================ $title ================"

  $options = $options | ConvertFrom-Json

  foreach ($option in $options) {
    $index = $options.IndexOf($option) + 1
    Write-Host "$($index): Press '$($index)' for $($option.displayName)."
  }

  $selection = promptForAnswer('Please make a selection')

  return $options[$selection - 1]
}

function PromptForAnswer {
  param(
    [Parameter(Mandatory = $true)]
    [string]$prompt
  )

  $selection = $null

  do {
    $selection = Read-Host $prompt
  } until ($null -ne $selection)

  return $selection
}

function PromptForAzureRegion() {
  $locations = az account list-locations
  return Show-Menu -title 'Azure Resource Region' -options $locations
}

function PromptForApplicationType() {
  $options = "[
    { 'name': 'function', 'displayName': 'Function App' }
  ]"

  return Show-Menu -title 'Azure app service type' -options $options
}

Clear-Host

PrintLogo

$azureDevOpsOrganization = PromptForAnswer('Please enter your Azure DevOps Organization name (e.g. the MyOrganization in https://dev.azure.com/MyOrganization)')
$azureDevOpsProject = PromptForAnswer('Please enter a project name for your new Azure DevOps project')
$region = PromptForAzureRegion
$azureResourceGroupName = PromptForAnswer('Please enter a name for your Azure resource group')
$siteType = PromptForApplicationType
$azureSiteName = PromptForAnswer('Please enter a name for your Azure Function app')

az concierge create `
  --organization $azureDevOpsOrganization `
  --project $azureDevOpsProject `
  --location $region.name `
  --group-name $azureResourceGroupName `
  --site-type $siteType `
  --site-name $azureSiteName
