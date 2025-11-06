#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to create an unused access key for a given IAM user
def create_stale_access_key(user, region, profile):

    # Initiate session with boto3 for IAM
    session = boto3.Session(profile_name=profile, region_name=region)
    iam = session.client("iam")

    try:
        # Create a new access key
        response = iam.create_access_key(UserName=user)
        access_key = response["AccessKey"]["AccessKeyId"]

        print(f"Recipe applied: Created new (stale) access key for user '{user}'.")
        print(f"AccessKeyId: {access_key}")

    except ClientError as e:
        if e.response["Error"]["Code"] == "LimitExceeded":
            print(f"User '{user}' already has 2 active access keys. Delete one before creating a new one.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="INPUT IAM USERNAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        create_stale_access_key(args.user, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python apply_create_stale_access_key.py {IAM USERNAME} --profile FYP --region ap-southeast-1