# Azure VM Metadata Query Tool

This tool allows you to query Azure VM metadata and retrieve either the full structure or specific keys.

## Usage

```bash
python metadata_query/fetch_metadata.py
python metadata_query/fetch_metadata.py --key compute.name

## Testing
python -m unittest metadata_query/test_fetch_metadata.py

## Terraform (To create test VM)
cd terraform
terraform init
terraform apply