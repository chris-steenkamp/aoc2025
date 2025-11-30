"""Scaffolding for new day solutions.

Creates the necessary files for a new day's solution.
"""

from pathlib import Path

# Paths relative to this file
DAYS_DIR = Path(__file__).parent / "days"
TESTS_DIR = Path(__file__).parent.parent.parent / "tests"
DATA_DIR = Path(__file__).parent.parent.parent.parent.parent / "data"


def scaffold_day(day: int) -> None:
    """Scaffold a new day's solution files."""
    day_str = f"{day:02d}"

    # Create the day module file
    day_path = DAYS_DIR / f"day{day_str}.py"
    if day_path.exists():
        raise FileExistsError(f"Day {day} module already exists at {day_path}")

    day_template = _generate_day_template(day)
    day_path.write_text(day_template)
    print(f"  📄 Created: {day_path}")

    # Create the test file
    test_path = TESTS_DIR / f"test_day{day_str}.py"
    if not test_path.exists():
        test_template = _generate_test_template(day)
        test_path.write_text(test_template)
        print(f"  📄 Created: {test_path}")

    # Create the example input file
    example_path = DATA_DIR / "examples" / f"{day_str}.txt"
    if not example_path.exists():
        example_path.parent.mkdir(parents=True, exist_ok=True)
        example_path.write_text("# Paste example input here\n")
        print(f"  📄 Created: {example_path}")

    # Print instructions for manual step
    print()
    print("📝 Manual step required:")
    print(f"   Add the import to src/aoc2025/days/__init__.py:")
    print()
    print(f"   from . import day{day_str}")
    print()
    print(f"   And add to the DAYS dict:")
    print()
    print(f"   {day}: day{day_str},")


def _generate_day_template(day: int) -> str:
    """Generate the template for a new day module."""
    return f'''"""Day {day:02d}: [Title]

https://adventofcode.com/2025/day/{day}
"""


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = input_text.strip().split("\\n")

    # TODO: Implement solution
    return None


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\\n")

    # TODO: Implement solution
    return None
'''


def _generate_test_template(day: int) -> str:
    """Generate the template for a new test file."""
    day_str = f"{day:02d}"
    return f'''"""Tests for Day {day:02d}."""

import pytest

from aoc2025.days import day{day_str}


@pytest.fixture
def example_input(load_example):
    """Load the example input for day {day:02d}."""
    return load_example({day})


class TestPart1:
    """Tests for Part 1."""

    def test_example(self, example_input):
        """Test part one with the example input."""
        # TODO: Update expected value from puzzle description
        result = day{day_str}.part_one(example_input)
        assert result is None  # Replace with expected value


class TestPart2:
    """Tests for Part 2."""

    def test_example(self, example_input):
        """Test part two with the example input."""
        # TODO: Update expected value from puzzle description
        result = day{day_str}.part_two(example_input)
        assert result is None  # Replace with expected value
'''
