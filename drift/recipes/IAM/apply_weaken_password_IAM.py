#!/usr/bin/env python3

import argparse
import boto3
from botocore.exceptions import ClientError

def weaken_password_policy(region, profile):
    session = boto3.Session(profile_name=profile, region_name=region)
    iam = session.client("iam")

    # Weak password policy: minimal enforcement, no expiration
    weak_policy = {
        "MinimumPasswordLength": 6,
        "RequireSymbols": False,
        "RequireNumbers": False,
        "RequireUppercaseCharacters": False,
        "RequireLowercaseCharacters": False,
        "AllowUsersToChangePassword": True,
        "PasswordReusePrevention": 1,
        "HardExpiry": False
    }

    try:
        iam.update_account_password_policy(**weak_policy)
        print("Recipe applied: Password policy weakened for the AWS account.")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        weaken_password_policy(args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python apply_weaken_password_policy.py --profile FYP --region ap-southeast-1