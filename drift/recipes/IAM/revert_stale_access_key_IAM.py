#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to delete all but the primary access key for a user
def delete_stale_access_key(user, region, profile):

    # Initiate session with boto3 for IAM
    session = boto3.Session(profile_name=profile, region_name=region)
    iam = session.client("iam")

    try:
        keys = iam.list_access_keys(UserName=user)["AccessKeyMetadata"]

        if len(keys) <= 1:
            print(f"No stale access keys found for '{user}'.")
            return

        # Delete all keys except the oldest one (or keep first if you prefer)
        for key in keys[1:]:
            iam.delete_access_key(UserName=user, AccessKeyId=key["AccessKeyId"])
            print(f"Deleted stale key: {key['AccessKeyId']}")

        print(f"Recipe reverted: Removed stale IAM access keys for '{user}'.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="INPUT IAM USERNAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        delete_stale_access_key(args.user, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python revert_stale_access_key_IAM.py {IAM USERNAME} --profile FYP --region ap-southeast-1