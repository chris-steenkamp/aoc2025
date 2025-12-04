"""CLI for Advent of Code 2025 solutions.

Usage:
    uv run aoc solve <day> [--part <1|2>]
    uv run aoc download <day>
    uv run aoc new <day>
"""

import time
from pathlib import Path

import click
from dotenv import load_dotenv

from . import input as aoc_input
from .days import run_day
from .scaffold import scaffold_day

# Load .env from project root
env_path = Path(__file__).parent.parent.parent.parent.parent / ".env"
load_dotenv(env_path)


@click.group()
@click.version_option()
def main():
    """Advent of Code 2025 Solutions in Python."""
    pass


@main.command()
@click.argument("day", type=click.IntRange(1, 25))
@click.option("--part", "-p", type=click.IntRange(1, 2), help="Run only part 1 or 2")
def solve(day: int, part: int | None):
    """Run a specific day's solution."""
    click.echo(f"Advent of Code 2025 - Day {day:02d}")
    click.echo("=" * 40)

    # Get input (auto-download if missing)
    try:
        input_text = aoc_input.get_input(day)
    except Exception as e:
        click.echo(f"❌ Failed to get input: {e}", err=True)
        raise SystemExit(1)

    # Run the solution(s)
    if part is not None:
        _run_part(day, part, input_text)
    else:
        _run_part(day, 1, input_text)
        click.echo()
        _run_part(day, 2, input_text)


def _run_part(day: int, part: int, input_text: str):
    """Run a single part and display the result with timing."""
    start = time.perf_counter()
    result = run_day(day, part, input_text)
    elapsed = (time.perf_counter() - start) * 1000

    if result is not None:
        click.echo(f"Part {part}: {result}")
        click.echo(f"{elapsed:.3f}ms")
    else:
        click.echo(f"Part {part}: Not implemented yet")


@main.command()
@click.argument("day", type=click.IntRange(1, 25))
def download(day: int):
    """Download input for a day."""
    click.echo(f"📥 Downloading input for Day {day:02d}...")

    try:
        path = aoc_input.download_input(day)
        click.echo(f"✅ Input saved to: {path}")
    except Exception as e:
        click.echo(f"❌ Failed to download: {e}", err=True)
        raise SystemExit(1)


@main.command()
@click.argument("day", type=click.IntRange(1, 25))
def new(day: int):
    """Scaffold a new day's solution files."""
    click.echo(f"🆕 Scaffolding Day {day:02d}...")

    try:
        scaffold_day(day)
        click.echo(f"✅ Day {day:02d} scaffolded successfully!")
    except Exception as e:
        click.echo(f"❌ Failed to scaffold: {e}", err=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
