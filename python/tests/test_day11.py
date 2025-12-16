"""Tests for Day 11."""

import pytest
from aoc2025.days import day11


@pytest.fixture
def example_input(load_example):
    """Load the example input for day 11."""
    return load_example(11)


class TestPart1:
    """Tests for Part 1."""

    def test_example(self, example_input):
        """Test part one with the example input."""
        # TODO: Update expected value from puzzle description
        result = day11.part_one(example_input)
        assert result == 5  # Replace with expected value


class TestPart2:
    """Tests for Part 2."""

    def test_example(self, example_input):
        example_input = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
        """Test part two with the example input."""
        # TODO: Update expected value from puzzle description
        result = day11.part_two(example_input)
        assert result == 2  # Replace with expected value
