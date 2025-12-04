"""Tests for Day 01."""

import pytest
from aoc2025.days import day01


@pytest.fixture
def example_input(load_example):
    """Load the example input for day 01."""
    return load_example(1)


class TestPart1:
    """Tests for Part 1."""

    def test_example(self, example_input):
        """Test part one with the example input."""
        # TODO: Update expected value from puzzle description
        result = day01.part_one(example_input)
        assert result == 3  # Replace with expected value


class TestPart2:
    """Tests for Part 2."""

    def test_example(self, example_input):
        """Test part two with the example input."""
        # TODO: Update expected value from puzzle description
        result = day01.part_two(example_input)
        assert result == 6  # Replace with expected value
