# Recipe registry
RECIPE_REGISTRY = {
    "s3": {
        "apply": [
            "apply_public_policy_s3",
            "apply_public_s3",
            "apply_versioning_disable_s3"
        ],
        "revert": [
            "revert_public_policy_s3",
            "revert_public_s3",
            "revert_versioning_disable_s3"
        ]
    },
    "iam": {
        "apply": [
            "apply_stale_access_key_IAM",
            "apply_weaken_password_IAM",
            "apply_wildcard_IAM"
        ],
        "revert": [
            "revert_stale_access_key_IAM",
            "revert_weaken_password_IAM",
            "revert_wildcard_IAM"
        ]
    },
    "sg": {
        "apply": [
            "apply_open_egress_SG",
            "apply_open_ingress_SG"
        ],
        "revert": [
            "revert_open_egress_SG",
            "revert_open_ingress_SG"
        ]
    }
}

# Helper functions
def get_recipe(service: str, action: str) -> list[str]:
    return RECIPE_REGISTRY.get(service, {}).get(action, [])

def list_services()-> list[str]:
    return list(RECIPE_REGISTRY.keys())