"""Tests for Day 04."""

import pytest
from aoc2025.days import day04


@pytest.fixture
def example_input(load_example):
    """Load the example input for day 04."""
    return load_example(4)


class TestPart1:
    """Tests for Part 1."""

    def test_example(self, example_input):
        """Test part one with the example input."""
        # TODO: Update expected value from puzzle description
        result = day04.part_one(example_input)
        assert result == 13  # Replace with expected value


class TestPart2:
    """Tests for Part 2."""

    def test_example(self, example_input):
        """Test part two with the example input."""
        # TODO: Update expected value from puzzle description
        result = day04.part_two(example_input)
        assert result is None  # Replace with expected value
