# Provider Configuration:
provider "aws" {
    # Profile to use from the AWS credentials file
    profile = var.aws_profile
    region  = var.aws_region
}

# S3 Bucket Resource for storing remote state:
resource "aws_s3_bucket" "tf_state" {
    bucket = ${var.s3_bucket_name}

    tags = {
        Name        = "Terraform State Bucket"
        Environment = "Dev"
    }
}

# Enable versioning on the S3 bucket:
resource "aws_s3_bucket_versioning" "tf_state_versioning" {
    bucket = aws_s3_bucket.tf_state.id

    versioning_configuration {
        status = "Enabled"
    }
}

# Enable server-side encryption on the S3 bucket:
resource "aws_s3_bucket_server_side_encryption_configuration" "tf_state_encryption" {
    bucket = aws_s3_bucket.tf_state.id

    rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
    }
}

# Disable public access to the S3 bucket:
resource "aws_s3_bucket_public_access_block" "tf_state_public_access" {
    bucket = aws_s3_bucket.tf_state.id
    block_public_acls       = true
    block_public_policy     = true
    ignore_public_acls      = true
    restrict_public_buckets = true
}

# DynamoDB Table Resource:
resource "aws_dynamodb_table" "tf_lock" {
    name = var.dynamodb_table_name
    hash_key = "LockID"
    billing_mode = "PAY_PER_REQUEST"

    attribute {
        name = "LockID"
        type = "S"
    }

    tags = {
        Name        = "Terraform Lock Table"
        Environment = "Dev"
    }
}