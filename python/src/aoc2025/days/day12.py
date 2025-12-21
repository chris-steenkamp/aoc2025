"""Day 12: [Title]

https://adventofcode.com/2025/day/12
"""

from aoc2025.utils.grid import Grid
from aoc2025.utils.parsing import parse_groups


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    groups = parse_groups(input_text)
    shapes = {}
    for g in groups[:-1]:
        index, shape = g.split("\n", 1)
        shapes[int(index[:-1])] = Grid.from_string(shape)

    regions = []
    a = 0
    for g in groups[-1].split("\n"):
        size, presents = g.split(":", 1)
        x, y = size.split("x")
        grid = Grid.filled(int(x), int(y), ".")
        presents = list(map(int, [p for p in presents.split(" ") if p]))
        regions.append(
            (
                grid,
                presents,
            )
        )

    for grid, presents in regions:
        area = grid.height * grid.width
        shape_area = 0
        for i, p in enumerate(presents):
            if p == 0:
                continue

            shape_area += len(shapes[i].find_all("#")) * p

        if shape_area <= area:
            a += 1

    return a


def part_two(_: str) -> int | None:
    """Solve part two."""
    return 0
