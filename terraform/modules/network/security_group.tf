resource "azurerm_network_security_group" "nsg" {
  name                = "${var.app_name}-sg"
  location            = var.location
  resource_group_name = azurerm_resource_group.tf_devops.name

  security_rule {
    name                       = "SSH"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

  tags = var.tags
}

resource "azurerm_subnet_network_security_group_association" "nsg_association" {
  subnet_id                 = azurerm_subnet.tf_subnet.id
  network_security_group_id = azurerm_network_security_group.nsg.id
}
