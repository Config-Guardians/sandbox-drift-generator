# Create a secure IAM user that can access S3 bucket for drift application:

resource "aws_iam_user" "sandbox_user" {
    name = "${var.project_prefix}-sandbox-user"
    tags = var.tags
}

# Least privilege policy allowing only access to S3 bucket created in the sandbox
resource "aws_iam_user_policy" "sandbox_user_policy" {
    name = "${var.project_prefix}-s3-access-policy"
    user = aws_iam_user.sandbox_user.name

    policy = jsonencode({
        Version = "2012-10-17"
        Statement = [
        {
            Sid = "AllowS3BucketAccess"
            Effect = "Allow"
            Action = [
            "s3:GetObject",
            "s3:PutObject",
            "s3:ListBucket"
            ]
            Resource = [
            var.test_bucket_arn,
            "${var.test_bucket_arn}/*"
            ]
        }
        ]
    })
}