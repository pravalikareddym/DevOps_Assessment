# 3-Tier Architecture on Azure with Terraform and Python

## Stack
- Azure Kubernetes Service (AKS)
- Python (Flask) for Web and App tiers
- Terraform for Infrastructure as Code

## NFR
- At least 3 instances across zones a/b/c always UP
- Ensured via:
  - AKS node pool in zones 1/2/3
  - Kubernetes deployments with 3 replicas
  - Pod Anti-Affinity
  - PodDisruptionBudget

## How to Use
```bash
# Init
terraform init

# Plan
terraform plan -var-file="environments/dev/terraform.tfvars"

# Apply
terraform apply -var-file="environments/dev/terraform.tfvars"

# Build & Push containers
cd app/web && docker build -t <registry>/web:latest . && docker push <registry>/web:latest
cd ../app && docker build -t <registry>/app:latest . && docker push <registry>/app:latest

# Deploy
kubectl apply -f k8s/
