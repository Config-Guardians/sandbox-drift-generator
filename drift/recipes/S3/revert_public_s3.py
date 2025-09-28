#!/usr/bin/env python3

# Imports
import argparse
import boto3
from boto3.exceptions import ClientError

# Function to make bucket private
def make_bucket_private(bucket, region, profile):

    # Initiate session with boto3 for s3
    session = boto3.session(profile_name=profile, region_name=region)
    s3 = session.client("s3")

    # Restore public access block
    public_access_block = {
        "BlockPublicAcls": True,
        "IgnorePublicAcls": True,
        "BlockPublicPolicy": True,
        "RestrictPublicBuckets": True,
    }
    s3.put_public_access_block(Bucket=bucket, PublicAccessBlockConfiguration=public_access_block)

    # Set bucket ACL to private
    s3.put_bucket_acl(Bucket=bucket, ACL="private")

    # Remove bucket policies
    try:
        s3.delete_bucket_policy(Bucket=bucket)
    except ClientError as e:
        # If there were no policies, then we don't raise error
        if e.response["Error"]["Code"] != "NoSuchBucketPolicy":
            raise

    print("Recipe applied, bucket is now private")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket", help="INSERT NAME OF S3 BUCKET")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        make_bucket_private(args.bucket, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command: python rever_s3_public.py my-sandbox-bucket --profile FYP --region ap-southeast-1