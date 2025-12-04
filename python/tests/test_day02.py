"""Tests for Day 02."""

import pytest
from aoc2025.days import day02


@pytest.fixture
def example_input(load_example):
    """Load the example input for day 02."""
    return load_example(2)


class TestPart1:
    """Tests for Part 1."""

    def test_example(self, example_input):
        """Test part one with the example input."""
        # TODO: Update expected value from puzzle description
        result = day02.part_one(example_input)
        assert result == 1227775554  # Replace with expected value


class TestPart2:
    """Tests for Part 2."""

    def test_example(self, example_input):
        """Test part two with the example input."""
        # TODO: Update expected value from puzzle description
        result = day02.part_two(example_input)
        assert result == 4174379265  # Replace with expected value
