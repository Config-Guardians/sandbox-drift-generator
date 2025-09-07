# This file is used to indicate the outputs that will be displayed after the Terraform run

# This will output the AWS account ID
output "account_id" {
  description = "AWS account ID"
  value       = data.aws_caller_identity.current.account_id
}

# This will output the S3 bucket name
output "bucket_name" {
  description = "S3 bucket name"
  value       = aws_s3_bucket.demo_bucket.id
}