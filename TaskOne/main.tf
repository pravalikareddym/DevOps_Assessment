module "aks_cluster" {
  source              = "./modules/aks_cluster"
  resource_group_name = "my-resource-group"
  location            = "eastus"
  cluster_name        = "my-aks-cluster"
  node_count          = var.node_count
  zones               = var.zones
}