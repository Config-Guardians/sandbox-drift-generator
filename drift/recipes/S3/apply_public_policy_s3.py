#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to attach an over-permissive policy
def apply_over_permissive_policy(bucket, region, profile):

    # Initiate session with boto3 for S3
    session = boto3.Session(profile_name=profile, region_name=region)
    s3 = session.client("s3")

    # Dangerous, world-readable policy
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "AllowPublicReadWrite",
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject", "s3:PutObject", "s3:DeleteObject"],
                "Resource": f"arn:aws:s3:::{bucket}/*"
            }
        ]
    }

    try:
        s3.put_bucket_policy(Bucket=bucket, Policy=str(policy).replace("'", '"'))
        print(f"Recipe applied: Over-permissive policy attached to '{bucket}'.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket", help="INPUT S3 BUCKET NAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        apply_over_permissive_policy(args.bucket, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python apply_over_permissive_policy.py {INSERT NAME OF BUCKET} --profile FYP --region ap-southeast-1
