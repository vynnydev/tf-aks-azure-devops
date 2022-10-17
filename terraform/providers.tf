terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "=3.14.0"
    }
  }

  backend "azurerm" {
    resource_group_name = "tf"
    storage_account_name = "stgaccount135246"
    container_name = "tf-stg-container"
    key            = "tf-azure/terraform.tfstate"
  }
}

provider "azurerm" {
  features {}
}
