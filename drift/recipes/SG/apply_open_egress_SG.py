#!/usr/bin/env python3

# Imports
import argparse
import boto3
from botocore.exceptions import ClientError

# Function to open outbound (0.0.0.0/0) on the security group
def open_egress(sg_id, region, profile):

    # Initiate boto3 session
    session = boto3.Session(profile_name=profile, region_name=region)
    ec2 = session.client("ec2")

    try:
        # Authorize unrestricted outbound traffic
        ec2.authorize_security_group_egress(
            GroupId=sg_id,
            IpPermissions=[
                {
                    "IpProtocol": "-1",  # all protocols
                    "FromPort": -1,
                    "ToPort": -1,
                    "IpRanges": [{"CidrIp": "0.0.0.0/0", "Description": "Drift: Open egress"}],
                }
            ],
        )
        print(f"Recipe applied: Egress opened to 0.0.0.0/0 on SG '{sg_id}'.")
    except ClientError as e:
        if "InvalidPermission.Duplicate" in str(e):
            print("Egress already open to 0.0.0.0/0.")
        else:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sg_id", help="INPUT SECURITY GROUP ID")
    parser.add_argument("--profile", help="FYP")
    parser.add_argument("--region", help="ap-southeast-1")
    args = parser.parse_args()

    try:
        open_egress(args.sg_id, args.region, args.profile)
    except ClientError as e:
        print(f"Error: {e}")

# Helper command:
# python apply_open_egress_S3.py {SECURITY_GROUP_ID} --profile FYP --region ap-southeast-1
