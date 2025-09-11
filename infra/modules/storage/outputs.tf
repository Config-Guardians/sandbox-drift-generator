# Outputs S3 information for drift generator
output "test_bucket_name" { value = aws_s3_bucket.test.id }
output "test_bucket_arn"  { value = aws_s3_bucket.test.arn }