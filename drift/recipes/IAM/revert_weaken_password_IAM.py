#!/usr/bin/env python3

import argparse
import boto3
from botocore.exceptions import ClientError

def restore_password_policy(region, profile):
    session = boto3.Session(profile_name=profile, region_name=region)
    iam = session.client("iam")

    strong_policy = {
        "MinimumPasswordLength": 14,
        "RequireSymbols": True,
        "RequireNumbers": True,
        "RequireUppercaseCharacters": True,
        "RequireLowercaseCharacters": True,
        "AllowUsersToChangePassword": True,
        "MaxPasswordAge": 90,
        "PasswordReusePrevention": 24,
        "HardExpiry": False
    }

    try:
        iam.update_account_password_policy(**strong_policy)
        print("Recipe reverted: Strong password policy restored for the AWS account.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        restore_password_policy(args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python revert_weaken_password_IAM.py --profile FYP --region ap-southeast-1