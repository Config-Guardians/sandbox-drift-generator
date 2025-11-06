#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to remove open ingress rule
def close_ingress(sg_id, region, profile):

    # Initiate session with boto3 for EC2
    session = boto3.Session(profile_name=profile, region_name=region)
    ec2 = session.client("ec2")

    try:
        ec2.revoke_security_group_ingress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    "IpProtocol": "-1",
                    "FromPort": -1,
                    "ToPort": -1,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0"}],
                }
            ],
        )
        print(f"Recipe reverted: Removed open ingress (0.0.0.0/0) from SG '{sg_id}'.")
    except ClientError as e:
        if "InvalidPermission.NotFound" in str(e):
            print("No open ingress rule found — already reverted.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sg_id", help="INPUT SECURITY GROUP ID")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        close_ingress(args.sg_id, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python revert_open_ingress_SG.py {SECURITY_GROUP_ID} --profile FYP --region ap-southeast-1