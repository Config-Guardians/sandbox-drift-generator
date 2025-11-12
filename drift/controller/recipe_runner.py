import subprocess
import sys
from pathlib import Path

# Function to run recipe
def run_recipe(service: str, recipe_name: str, args: list[str]) -> None:
    # Building the path to the recipe file
    recipe_path = Path(f"recipes/{service}/{recipe_name}.py")

    if not recipe_path.exists():
        print(f"ERROR: Recipe not found at {recipe_path}")

    try:
        cmd = ["python3", str(recipe_path)] + args
        print(f"[RUNNING] {' '.join(cmd)}")

        process = subprocess.Popen(
            cmd,
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        process.wait()

        if process.returncode == 0:
            print(f"[SUCCESS] {recipe_name} completed successfully.\n")
        else:
            print(f"[FAILED] {recipe_name} exited with code {process.returncode}\n")
    
    except Exception as e:
        print(f"[EXCEPTION] Error running {recipe_name}: {e}")
