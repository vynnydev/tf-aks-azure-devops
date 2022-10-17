resource "azurerm_storage_account" "stg_account" {
  name                     = "stgaccount135246"
  resource_group_name      = azurerm_resource_group.tf_devops.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "GRS"

  blob_properties {
    versioning_enabled = true
  }

  tags = var.tags
}

resource "azurerm_storage_container" "stg_container" {
  name                 = "${var.app_name}-stg-container"
  storage_account_name = azurerm_storage_account.stg_account.name
}
