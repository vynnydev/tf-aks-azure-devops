terraform {
  azurerm = {
    source = "hashicorp/azurerm"
    version = "=3.0.1"
  }
}

provider "azurerm" {
  features {}
}

