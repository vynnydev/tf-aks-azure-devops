terraform {
  required_providers {
  azurerm = {
      source = "hashicorp/azurerm"
      version = "=3.0.1"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "aks_devops" {
  name = "aks-devops"
  location = "Brazil South"
}
