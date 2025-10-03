# Create a secure test bucket for drift application:

resource "random_id" "suffix" {
    byte_length = 4
}

resource "aws_s3_bucket" "test" {
    bucket = "${var.project_prefix}-test-bucket-${random_id.suffix.hex}"
    force_destroy = var.test_force_destroy
    tags = var.tags
}

# Enable default encryption using AES256
resource "aws_s3_bucket_server_side_encryption_configuration" "test" {
    bucket = aws_s3_bucket.test.id
    rule {
        apply_server_side_encryption_by_default {
            sse_algorithm = "AES256"
        }
    }
}

# Enable versioning on the bucket
resource "aws_s3_bucket_versioning" "test" {
    bucket = aws_s3_bucket.test.id
    versioning_configuration {
        status = "Enabled"
    }
}

# Block public access to the bucket
resource "aws_s3_bucket_public_access_block" "test" {
    bucket = aws_s3_bucket.test.id
    block_public_acls       = false
    block_public_policy     = false
    ignore_public_acls      = false
    restrict_public_buckets = false
}