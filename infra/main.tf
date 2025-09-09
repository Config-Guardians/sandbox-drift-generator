# This file is used to specify the resources to be created and managed by Terraform under AWS
provider "aws" {
    region = var.region
    profile = "FYP" # AWS ClI profile to be used
}

# Who am I check:
data "aws_caller_identity" "current" {}

# S3 Demo Bucket
resource "aws_s3_bucket" "demo_bucket" {
    bucket = var.s3_bucket_name
    force_destroy = true # Allow deletion of non-empty bucket
    tags = {
        Environment = "dev"
        managed_by = "terraform"
    }
}

# Block public access to the bucket
resource "aws_s3_bucket_public_access_block" "block_public_access" {
    bucket = aws_s3_bucket.demo_bucket.id # Reference the S3 bucket created above
    block_public_acls       = true # Block public ACLs
    block_public_policy     = true # Block public policy
    ignore_public_acls      = true # Ignore public ACLs
    restrict_public_buckets = true # Restrict public buckets
}

# Turn off versioning for the bucket
resource "aws_s3_bucket_versioning" "versioning" {
    bucket = aws_s3_bucket.demo_bucket.id # Reference the S3 bucket created above
    versioning_configuration {
        status = "Suspended" # Turn off versioning
    }
}

# Enable default encryption for the bucket
resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
    bucket = aws_s3_bucket.demo_bucket.id # Reference the S3 bucket created above
    rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256" # Use AES256 encryption
        }
    }
}