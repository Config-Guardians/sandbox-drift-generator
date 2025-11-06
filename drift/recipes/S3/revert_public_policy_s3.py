#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to remove any custom bucket policy
def remove_bucket_policy(bucket, region, profile):

    # Initiate session with boto3 for S3
    session = boto3.Session(profile_name=profile, region_name=region)
    s3 = session.client("s3")

    try:
        s3.delete_bucket_policy(Bucket=bucket)
        print(f"Recipe reverted: All custom bucket policies removed from '{bucket}'.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchBucketPolicy":
            print(f"No bucket policy found for '{bucket}' — already secure.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket", help="INPUT S3 BUCKET NAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        remove_bucket_policy(args.bucket, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python revert_bucket_policy.py {INSERT NAME OF BUCKET} --profile FYP --region ap-southeast-1
