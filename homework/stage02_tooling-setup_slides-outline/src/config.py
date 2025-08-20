#config.py
#with load_env() and get_key() as in lecture
from dotenv import load_dotenv
from typing import Optional
from pathlib import Path
import os

load_dotenv()  # looks for a .env file in the current and parent directories
print(".env loaded (if present)")

def get_key(name: str, default: Optional[str] = None) -> Optional[str]:
    return os.getenv(name, default)

PROJECT_ROOT = Path.cwd()
DATA_DIR = PROJECT_ROOT / "data"

