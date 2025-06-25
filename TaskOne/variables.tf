variable "resource_group_name" {}
variable "location" {}
variable "cluster_name" {}
variable "node_count" { default = 3 }
variable "zones" {
  type    = list(string)
  default = ["1", "2", "3"]
}