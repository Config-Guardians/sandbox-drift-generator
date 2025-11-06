#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to disable versioning on the bucket
def disable_bucket_versioning(bucket, region, profile):

    # Initiate session with boto3 for S3
    session = boto3.Session(profile_name=profile, region_name=region)
    s3 = session.client("s3")

    try:
        # Suspend versioning
        s3.put_bucket_versioning(
            Bucket=bucket,
            VersioningConfiguration={"Status": "Suspended"}
        )
        print(f"Recipe applied: Versioning disabled on bucket '{bucket}'.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bucket", help="INPUT S3 BUCKET NAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        disable_bucket_versioning(args.bucket, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python apply_versioning_disable_s3.py {INSERT NAME OF BUCKET} --profile FYP --region ap-southeast-1