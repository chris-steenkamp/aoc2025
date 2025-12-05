"""Day 04: [Title]

https://adventofcode.com/2025/day/4
"""

from aoc2025.utils.grid import Grid


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    grid = Grid.from_string(input_text.strip())

    nice_neighbours = 0

    for (x, y), c in grid.iter():
        if c == "@" and (
            len(
                list(
                    filter(
                        lambda e: grid.get(e[0], e[1]) == "@",
                        grid.neighbors_diagonal(x, y),
                    )
                )
            )
            < 4
        ):
            nice_neighbours += 1

    return nice_neighbours


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
