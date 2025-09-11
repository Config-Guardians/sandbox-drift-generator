# Using random provider for unique suffixes
terraform {
  required_version = ">= 1.2"
  required_providers {
    aws    = { source = "hashicorp/aws" }
    random = { source = "hashicorp/random" }
  }
}