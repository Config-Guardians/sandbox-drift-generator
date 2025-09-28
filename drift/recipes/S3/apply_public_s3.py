#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to make bucket public
def make_bucket_public(bucket, region, profile):

    # Initiate session with boto3 for s3
    session = boto3.session(profile_name=profile, region_name=region)
    s3 = session.client("s3")

    # Turn off public access block
    public_access_block = {
        "BlockPublicAcls": False,
        "IgnorePublicAcls": False,
        "BlockPublicPolicy": False,
        "RestrictPublicBuckets": False,
    }
    s3.put_public_acess_block(Bucket=bucket, PublicAccessBlockConfiguration=public_access_block)

    # Set bucket ACL to public read
    s3.put_bucket_acl(Bucket=bucket, ACL="public-read")

    # Attach policy to allow access for getObject to public
    policy = {
        "Version": "2012-10-17",
        "Statement": [{
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": f"arn:aws:s3:::{bucket}/*"
        }]
    }
    s3.put_bucket_policy(Bucket=bucket, Policy=str(policy).replace("'", '"')) # Replacing single quotes with double quote

    print("Recipe applied, bucket is now public")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket", help="INPUT S3 BUCKET NAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        make_bucket_public(args.bucket, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command: python apply_s3_public.py my-sandbox-bucket --profile FYP --region ap-southeast-1