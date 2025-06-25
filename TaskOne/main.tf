module "aks_cluster" {
  source              = "./modules/aks_cluster"
  resource_group_name = var.resource_group_name
  location            = var.location
  cluster_name        = var.cluster_name
  node_count          = var.node_count
  zones               = var.zones
}