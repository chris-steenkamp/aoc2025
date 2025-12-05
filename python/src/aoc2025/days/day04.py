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
    grid = Grid.from_string(input_text.strip())

    nice_neighbours = 0
    old_val = nice_neighbours

    while True:
        to_remove = []
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
                to_remove.append((x, y))

        for x, y in to_remove:
            grid.set(x, y, ".")

        if len(to_remove) == 0:
            break

    return nice_neighbours
