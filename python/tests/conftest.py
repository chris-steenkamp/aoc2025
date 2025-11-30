"""pytest configuration and fixtures for AoC tests."""

from pathlib import Path

import pytest

# Path to data directory
DATA_DIR = Path(__file__).parent.parent.parent / "data"


@pytest.fixture
def load_example():
    """Factory fixture to load example input for a given day."""
    def _load_example(day: int) -> str:
        path = DATA_DIR / "examples" / f"{day:02d}.txt"
        if not path.exists():
            pytest.skip(f"Example input not found: {path}")
        return path.read_text()
    return _load_example


@pytest.fixture
def load_input():
    """Factory fixture to load puzzle input for a given day."""
    def _load_input(day: int) -> str:
        path = DATA_DIR / "inputs" / f"{day:02d}.txt"
        if not path.exists():
            pytest.skip(f"Puzzle input not found: {path}")
        return path.read_text()
    return _load_input


@pytest.fixture
def example_input(load_example):
    """Convenience fixture - override in test files to specify the day."""
    # This should be overridden in individual test files
    pytest.skip("Override example_input fixture with specific day")
