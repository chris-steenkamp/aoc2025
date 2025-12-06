"""Day 06: [Title]

https://adventofcode.com/2025/day/6
"""

from math import prod

from aoc2025.utils.grid import Grid
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
    lines = input_text.split("\n")

    grid = Grid(lines[:-2]).rotate_left()

    inputs = ["".join(grid.row(y)).strip() for y in range(grid.height)]
    opcodes = list(reversed([opcode for opcode in lines[-2].split()]))

    opcode_index = 0
    opcode = opcodes[opcode_index]
    subtotal = 0 if opcode == "+" else 1
    total = 0

    for val in inputs:
        if val:
            subtotal = operations[opcode]([subtotal, int(val)])
        else:
            # we've found a blank which means we start processing the next operation
            opcode_index += 1
            total += subtotal
            opcode = opcodes[opcode_index]
            subtotal = 0 if opcode == "+" else 1

    # finally add the last calculated subtotal back to the total
    total += subtotal

    return total
