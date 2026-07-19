variable "aws_region" {
  description = "AWS region for the EC2 instance"
  type        = string
  default     = "us-east-2"
}

variable "ami_id" {
  description = "AMI used for the EC2 instance"
  type        = string
  default     = "ami-097a2df4ac947655f"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "project_name" {
  description = "Prefix used when naming Terraform-managed resources"
  type        = string
  default     = "ec2-apache"
}

variable "key_name" {
  description = "Name of the AWS key pair to create"
  type        = string
  default     = "aws_key"
}

variable "public_key" {
  description = "SSH public key material for the EC2 key pair"
  type        = string
}
