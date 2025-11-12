import json
from pathlib import Path

# Function to parse the TF output
def parse_tf_output(output_path: str) -> dict:
    
    path = Path(output_path)
    if not path.exists():
        raise FileNotFoundError(f"Terraform output file not found in {output_path}")
    
    with path.open() as f:
        data = json.load(f)

    # Normalized Dict per service
    dict = {"s3": [], "sg": [], "iam": []}

    # S3 parse (Bucket name)
    if "test_bucket_name" in data:
        s3_data = {
            "name": data["test_bucket_name"]["value"]
        }
    dict["s3"].append(s3_data)
    
    # SG parse (SG ID)
    if "sandbox_sg_id" in data:
        sg_data = {
            "id": data["sandbox_sg_id"]["value"]
        }
    dict["sg"].append(sg_data)

    # IAM parse (IAM name)
    if "sandbox_user_name" in data:
        iam_data = {
            "name": data["sandbox_user_name"]["value"]
        }
    dict["iam"].append(iam_data)

    return dict