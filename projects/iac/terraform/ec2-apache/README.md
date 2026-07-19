# EC2 Apache

An infrastructure-as-code example that provisions an AWS EC2 instance with Terraform and bootstraps Apache through cloud-init.

## What It Demonstrates

- Terraform resource composition for EC2, key pairs, and security groups
- Basic AWS networking exposure for SSH and HTTP
- Cloud-init user data to install and start Apache at launch
- Exporting instance connection details with Terraform outputs
- Template-driven cloud-init with a user-supplied SSH public key

## Files

- `main.tf` defines the EC2 instance, key pair, and security groups.
- `provider.tf` and `version.tf` pin the AWS provider and Terraform version.
- `variables.tf` keeps region, key pair, and SSH public key configurable.
- `scripts/apache-mkdocs.yaml.tftpl` contains the cloud-init bootstrap logic as a Terraform template.

## Requirements

- AWS credentials configured for the target account
- An SSH public key you want Terraform to register as an EC2 key pair
- A subnet in the target region that can assign a public IPv4 address to the instance

## Run

```bash
cd projects/iac/terraform/ec2-apache
terraform init
terraform apply -var='public_key=ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... you@host'
```

## Notes

- `public_key` is required. You can pass it with `-var='public_key=...'` or place it in `terraform.tfvars`.
- `key_name` defaults to `aws_key`, but you can override it if that name is already used in your account.
- The instance is configured for public HTTP access on port `80` and public SSH access on port `22`.
- The same `public_key` value is injected into cloud-init for the `spiderman` user's `ssh_authorized_keys`.
- The current example does not configure TLS or DNS. Access the page with `http://<public_ip>` after deployment.
- This showcase copy intentionally excludes `.tfstate`, provider caches, and private key material.

## Cleanup

Terraform will continue to manage billable AWS resources until you destroy them. When you are done with the example, run:

```bash
terraform destroy -var='public_key=ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... you@host'
```

If you used `terraform.tfvars`, a plain `terraform destroy` is enough.

## Optional terraform.tfvars

```hcl
public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... you@host"
key_name   = "my-aws-key"
```

With a `terraform.tfvars` file in place, you can run:

```bash
terraform apply
```
