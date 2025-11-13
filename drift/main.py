from rich.prompt import IntPrompt
from rich.console import Console
from rich.panel import Panel
from controller.controller import DriftController
from controller.utils import info
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_PATH = BASE_DIR.parent / "outputs.json"

console = Console()

# --- UI Functions ---

def show_main_menu(controller: DriftController):
    console.clear()
    resources = controller.list_resources()

    s3 = resources["s3"][0]["name"] if resources["s3"] else "—"
    iam = resources["iam"][0]["name"] if resources["iam"] else "—"
    sg = resources["sg"][0]["id"] if resources["sg"] else "—"

    body = (
        f"Profile: {controller.profile}      Region: {controller.region}\n"
        "──────────────────────────────────────────────\n"
        f"Resources Loaded:\n• S3 : {s3}\n• IAM : {iam}\n• SG : {sg}\n"
        "──────────────────────────────────────────────\n"
        "[1] Apply S3 Drift       [4] Revert S3 Drift\n"
        "[2] Apply IAM Drift      [5] Revert IAM Drift\n"
        "[3] Apply SG Drift       [6] Revert SG Drift\n"
        "──────────────────────────────────────────────\n"
        "\\[r] Reload TF Output   \\[q] Quit\n"  # escape brackets so they render literally
        "──────────────────────────────────────────────"
    )
    console.print(Panel.fit(body, title="[bold cyan]Main Menu[/bold cyan]"), markup=True)


def select_and_run(controller: DriftController, service: str, action: str):
    """Displays recipes for a given service/action and handles navigation."""
    while True:
        recipes = controller.list_recipes(service, action)
        if not recipes:
            console.print(f"[red]No {action} recipes found for {service.upper()}[/red]")
            console.input("[Press Enter to go back]")
            return

        console.clear()
        body = (
            f"[bold cyan]{service.upper()} {action.upper()} RECIPES[/bold cyan]\n"
            "──────────────────────────────────────────────\n" +
            "\n".join([f"{i+1}. {r}" for i, r in enumerate(recipes)]) +
            "\n\\[b] Back\n──────────────────────────────────────────────"
        )
        console.print(Panel.fit(body, title=f"{service.upper()} ({action.upper()})"), markup=True)

        choice = console.input("[bold yellow]> Enter number or [b] back:[/bold yellow] ").strip().lower()
        if choice == "b":
            break
        if not choice.isdigit():
            console.print("[red]Invalid input[/red]")
            continue

        idx = int(choice) - 1
        if idx not in range(len(recipes)):
            console.print("[red]Invalid selection[/red]")
            continue

        recipe = recipes[idx]
        console.print(f"\n[bold cyan]Executing {recipe}...[/bold cyan]")
        if action == "apply":
            controller.apply_drift(service, recipe)
        else:
            controller.revert_drift(service, recipe)

        console.input("[bold green]Press Enter to return to recipe list...[/bold green]")


# --- Main Loop ---

def main():
    controller = DriftController(str(OUTPUT_PATH), profile="FYP", region="ap-southeast-1")

    info("Configuration Guardian Drift Console initialized.")
    console.input("[bold green]Press Enter to start...[/bold green]")

    while True:
        show_main_menu(controller)
        choice = console.input("[bold yellow]> Enter choice:[/bold yellow] ").strip().lower()

        if choice == "q":
            break
        elif choice == "r":
            controller = DriftController(str(OUTPUT_PATH), "FYP", "ap-southeast-1")
            info("Terraform output reloaded.")
            console.input("[Press Enter to continue]")
        elif choice == "1":
            select_and_run(controller, "s3", "apply")
        elif choice == "2":
            select_and_run(controller, "iam", "apply")
        elif choice == "3":
            select_and_run(controller, "sg", "apply")
        elif choice == "4":
            select_and_run(controller, "s3", "revert")
        elif choice == "5":
            select_and_run(controller, "iam", "revert")
        elif choice == "6":
            select_and_run(controller, "sg", "revert")

    console.clear()
    console.print("[bold red]Exiting Configuration Guardian Drift Console.[/bold red]")


if __name__ == "__main__":
    main()