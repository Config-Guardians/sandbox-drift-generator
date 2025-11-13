from .tf_parser import parse_tf_output
from .recipe_runner import run_recipe
from .registry import get_recipe, list_services
from .utils import info, error

class DriftController:
    def __init__(self, tf_output_path: str, profile: str, region: str):
        self.resources = parse_tf_output(tf_output_path)
        self.profile = profile
        self.region = region

    # Methods
    def list_resources(self) -> dict:
        return self.resources
    
    def list_services(self) -> list[str]:
        return list_services()
    
    def list_recipes(self, service: str, action: str) -> list[str]:
        return get_recipe(service, action)
    
    def apply_drift(self, service: str, recipe_name: str):
        args = self._get_args(service)
        info(f"Applying drift: {service.upper()} → {recipe_name}")
        run_recipe(service, recipe_name, args)

    def revert_drift(self, service: str, recipe_name: str):
        args = self._get_args(service)
        info(f"Reverting drift: {service.upper()} → {recipe_name}")
        run_recipe(service, recipe_name, args)

    # Helper
    def _get_args(self, service: str) -> list[str]:
        if service == "s3":
            bucket = self.resources["s3"][0]["name"]
            return [bucket, "--profile", self.profile, "--region", self.region]
        elif service == "sg":
            sg_id = self.resources["sg"][0]["id"]
            return [sg_id, "--profile", self.profile, "--region", self.region]
        elif service == "iam":
            user = self.resources["iam"][0]["name"]
            return [user, "--profile", self.profile, "--region", self.region]
        else:
            error(f"Unknown service type: {service}")
            return []