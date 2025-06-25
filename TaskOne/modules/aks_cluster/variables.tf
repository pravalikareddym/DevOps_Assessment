variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "my-resource-group" 
}
variable "location" {
  description = "The Azure region where resources will be created"
  type        = string
  default     = "eastus"
}
variable "cluster_name" {
  description = "The name of the AKS cluster"
  type        = string
  default     = "my-aks-cluster"
}
variable "node_count" {
  description = "The number of nodes in the default node pool"
  type        = number
  default     = 3
}
variable "zones" {
  description = "The availability zones for the node pool"
  type        = list(string)
  default     = ["1", "2", "3"]
}