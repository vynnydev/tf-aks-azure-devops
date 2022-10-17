module "network" {
  source = "./modules/network"

  location = var.location
  app_name = var.app_name
  tags     = var.tags
}
