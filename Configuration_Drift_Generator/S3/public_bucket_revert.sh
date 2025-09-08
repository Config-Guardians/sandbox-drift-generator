#!/usr/bin/env bash
set -euo pipefail # Fail on error, undefined variable, or error in pipe

# Variables
PROFILE="FYP"
REGION="ap-southeast-1"
BUCKET_NAME="${1:?usage: $0 <bucket-name>}"

# Bucket existence check
aws --profile "$PROFILE" --region "$REGION" s3api head-bucket --bucket "$BUCKET_NAME" >/dev/null

echo "Reverting bucket '$BUCKET_NAME' to private in region '$REGION' with profile '$PROFILE'..."

# Update public access block settings to block public access
aws --profile "$PROFILE" --region "$REGION" s3api put-public-access-block \
  --bucket "$BUCKET_NAME" \
  --public-access-block-configuration \
  BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true

# Remove the bucket policy to revert it to private
aws --profile "$PROFILE" --region "$REGION" s3api delete-bucket-policy \
  --bucket "$BUCKET_NAME"
echo "Bucket '$BUCKET_NAME' is now private."

echo "Reversion complete."