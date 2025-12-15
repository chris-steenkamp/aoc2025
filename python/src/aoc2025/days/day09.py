"""Day 09: [Title]

https://adventofcode.com/2025/day/9
"""

import heapq

from aoc2025.utils.direction import Point, manhattan_distance
from aoc2025.utils.parsing import parse_unsigned


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    corners = list(
        map(Point, [parse_unsigned(p) for p in input_text.strip().split("\n")])
    )

    distances = []

    for i, p1 in enumerate(corners):
        for p2 in corners[i + 1 :]:
            heapq.heappush(distances, (-manhattan_distance(p1, p2), p1, p2))

    _, p1, p2 = heapq.heappop(distances)

    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
