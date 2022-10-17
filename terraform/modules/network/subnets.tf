resource "azurerm_subnet" "tf_subnet" {
  name                 = "${var.app_name}-subnet"
  resource_group_name  = azurerm_resource_group.tf_devops.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}
