import random
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from .registry import RECIPE_REGISTRY

console = Console()

def run_stress_test(controller, concurrency: int = 3):
    console.clear()
    console.rule("[bold yellow]Stress Test Mode[/bold yellow]")

    # Get all the recipes from the registry
    all_recipes = []
    for service, actions in RECIPE_REGISTRY.items():
        for recipe in actions["apply"]:
            all_recipes.append((service, recipe))

    if not all_recipes:
        console.print("[red]No recipes found for stress testing.[/red]")
        return

    # Pick 3 random recipes
    selected = random.sample(all_recipes, min(concurrency, len(all_recipes)))
    console.print(f"[cyan]Selected {len(selected)} recipes to apply concurrently:[/cyan]")
    for s, r in selected:
        console.print(f"• {s.upper()} → {r}")

    start_time = time.time()
    results = []

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {
            executor.submit(controller.apply_drift, service, recipe): (service, recipe)
            for service, recipe in selected
        }

        for future in as_completed(futures):
            service, recipe = futures[future]
            try:
                future.result()
                results.append((service, recipe, "SUCCESS"))
            except Exception as e:
                results.append((service, recipe, f"FAILED ({e})"))

    end_time = time.time()

    console.rule("[bold green]Stress Test Complete[/bold green]")
    for s, r, status in results:
        console.print(f"{s.upper()} – {r} → {status}")
    console.print(f"[bold cyan]Total time:[/bold cyan] {end_time - start_time:.2f}s")

    console.input("[bold green]Press Enter to return to main menu...[/bold green]")