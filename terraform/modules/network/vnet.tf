resource "azurerm_resource_group" "tf_devops" {
  name     = var.app_name
  location = var.location
}

resource "azurerm_virtual_network" "vnet" {
  name                = "${var.app_name}-vnet"
  location            = var.location
  resource_group_name = azurerm_resource_group.tf_devops.name
  address_space       = ["10.0.0.0/16"]
  dns_servers         = ["10.0.0.4", "10.0.0.5"]

  tags = var.tags
}
