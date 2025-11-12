from datetime import datetime

# --- Formatting helpers ---

def timestamp() -> str:
    """Return a simple timestamp string."""
    return datetime.now().strftime("%H:%M:%S")

def info(msg: str) -> None:
    print(f"[{timestamp()}] [INFO] {msg}")

def success(msg: str) -> None:
    print(f"[{timestamp()}] [SUCCESS] {msg}")

def error(msg: str) -> None:
    print(f"[{timestamp()}] [ERROR] {msg}")

def warn(msg: str) -> None:
    print(f"[{timestamp()}] [WARN] {msg}")
