"""Day 05: [Title]

https://adventofcode.com/2025/day/5
"""

from aoc2025.utils.parsing import parse_groups


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    ranges, ids = parse_groups(input_text)

    ids = [int(id) for id in ids.split("\n")]
    ranges = [r.split("-") for r in ranges.split("\n")]

    print(ranges)

    fresh_ids = 0

    for id in ids:
        for r in ranges:
            if int(r[0]) <= id <= int(r[1]):
                fresh_ids += 1
                break

    return fresh_ids


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
