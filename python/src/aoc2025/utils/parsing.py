"""Parsing utilities for Advent of Code.

Common functions for parsing puzzle inputs.
"""

import re


def parse_numbers(text: str) -> list[int]:
    """Parse all integers (positive and negative) from a string."""
    return [int(x) for x in re.findall(r"-?\d+", text)]


def parse_unsigned(text: str) -> list[int]:
    """Parse all unsigned integers from a string."""
    return [int(x) for x in re.findall(r"\d+", text)]


def parse_grid(text: str) -> list[list[str]]:
    """Parse input into a 2D grid of characters."""
    return [list(line) for line in text.strip().split("\n") if line]


def parse_lines(text: str) -> list[str]:
    """Parse input into lines, filtering empty lines."""
    return [line for line in text.strip().split("\n") if line]


def parse_groups(text: str) -> list[str]:
    """Parse input into groups separated by blank lines."""
    return [group.strip() for group in text.split("\n\n") if group.strip()]


def parse_line_numbers(line: str) -> list[int]:
    """Parse a line of space-separated numbers."""
    return [int(x) for x in line.split() if x.lstrip("-").isdigit()]


def parse_csv_numbers(line: str) -> list[int]:
    """Parse a line of comma-separated numbers."""
    return [int(x.strip()) for x in line.split(",") if x.strip().lstrip("-").isdigit()]
