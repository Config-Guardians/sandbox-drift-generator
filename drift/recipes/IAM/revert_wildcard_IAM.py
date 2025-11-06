#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to remove the over-permissive inline policy
def remove_wildcard_policy(user, region, profile):

    # Initiate boto3 session for IAM
    session = boto3.Session(profile_name=profile, region_name=region)
    iam = session.client("iam")

    policy_name = "WildcardFullAccess"

    try:
        iam.delete_user_policy(UserName=user, PolicyName=policy_name)
        print(f"Recipe reverted: Wildcard policy removed from IAM user '{user}'.")
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchEntity":
            print(f"No wildcard policy found for user '{user}' — already reverted.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user", help="INPUT IAM USERNAME")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        remove_wildcard_policy(args.user, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python revert_wildcard_IAM.py {IAM USERNAME} --profile FYP --region ap-southeast-1