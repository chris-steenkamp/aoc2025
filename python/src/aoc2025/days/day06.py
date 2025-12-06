"""Day 06: [Title]

https://adventofcode.com/2025/day/6
"""

from math import prod

from aoc2025.utils.parsing import parse_unsigned

operations = {"*": prod, "+": sum}


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = input_text.strip().split("\n")

    inputs = [parse_unsigned(line) for line in lines[:-1]]
    opcodes = [opcode for opcode in lines[-1].split()]

    total = sum(
        operations[opcode]((value[i] for value in inputs))
        for i, opcode in enumerate(opcodes)
    )
    return total


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
