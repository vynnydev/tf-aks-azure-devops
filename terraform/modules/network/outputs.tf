output "vnet_id" {
  value = azurerm_virtual_network.vnet.id
}

output "subnet_id" {
  value = azurerm_subnet.tf_subnet.id
}

output "security_group_id" {
  value = azurerm_network_security_group.nsg.id
}
