#!/usr/bin/env bash
set -euo pipefail # Fail on error, undefined variable, or error in pipe

# Variables
PROFILE="FYP"
REGION="ap-southeast-1"
BUCKET_NAME="${1:?usage: $0 <bucket-name>}"

# Bucket existence check
aws --profile "$PROFILE" --region "$REGION" s3api head-bucket --bucket "$BUCKET_NAME" >/dev/null

echo "Making bucket '$BUCKET_NAME' public in region '$REGION' with profile '$PROFILE'..."

# Update public access block settings to allow public access
aws --profile "$PROFILE" --region "$REGION" s3api put-public-access-block \
  --bucket "$BUCKET_NAME" \
  --public-access-block-configuration \
  BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=false,RestrictPublicBuckets=false

# This policy with the above settings will make the bucket publicly readable
POLICY=$(cat <<EOF
{
  "Version":"2012-10-17",
  "Statement":[{
    "Sid":"PublicRead",
    "Effect":"Allow",
    "Principal":"*",
    "Action":["s3:GetObject"],
    "Resource":["arn:aws:s3:::$BUCKET_NAME/*"]
  }]
}
EOF
)

# Apply the bucket policy to make it public
aws --profile "$PROFILE" --region "$REGION" s3api put-bucket-policy \
  --bucket "$BUCKET_NAME" \
  --policy "$POLICY"

echo "Bucket '$BUCKET_NAME' is now public."
