"""Input downloading and management for Advent of Code 2025.

Downloads puzzle inputs from adventofcode.com using the AOC_SESSION environment variable.
"""

import os
from pathlib import Path

import httpx

AOC_YEAR = 2025

# Path to data directory (relative to this file's location)
DATA_DIR = Path(__file__).parent.parent.parent.parent / "data"


def input_path(day: int) -> Path:
    """Get the path to the input file for a given day."""
    return DATA_DIR / "inputs" / f"{day:02d}.txt"


def get_input(day: int) -> str:
    """Get the input for a given day, downloading if necessary."""
    path = input_path(day)

    if path.exists():
        return path.read_text()
    else:
        print("📥 Input not found, downloading...")
        download_input(day)
        return path.read_text()


def download_input(day: int) -> str:
    """Download the input for a given day from adventofcode.com.

    Returns the path to the saved file.
    """
    session = os.environ.get("AOC_SESSION")
    if not session:
        raise ValueError(
            "AOC_SESSION environment variable not set.\n"
            'Set it with: $env:AOC_SESSION="your_session_cookie_value"\n'
            "Get the value from your browser's cookies at adventofcode.com"
        )

    url = f"https://adventofcode.com/{AOC_YEAR}/day/{day}/input"

    response = httpx.get(
        url,
        cookies={"session": session},
        headers={"User-Agent": "github.com/yourusername/aoc2025 by your@email.com"},
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"Failed to download input: HTTP {response.status_code} - {response.text}"
        )

    content = response.text
    path = input_path(day)

    # Ensure the directory exists
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)

    return str(path)
