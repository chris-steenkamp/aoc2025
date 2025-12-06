"""Day 05: [Title]

https://adventofcode.com/2025/day/5
"""

from aoc2025.utils.parsing import parse_groups


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    ranges, ids = parse_groups(input_text)

    ids = [int(id) for id in ids.split("\n")]
    ranges = [
        (int(r[0]), int(r[1])) for r in [r.split("-") for r in ranges.split("\n")]
    ]

    fresh_ids = 0

    for id in ids:
        for lower, upper in ranges:
            if lower <= id <= upper:
                fresh_ids += 1
                break

    return fresh_ids


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    ranges, _ = parse_groups(input_text)

    ranges = [
        (int(r[0]), int(r[1])) for r in [r.split("-") for r in ranges.split("\n")]
    ]

    fresh_ids = 0

    ranges = sorted(ranges)
    new_ranges = [ranges[0]]

    for lower, upper in ranges[1:]:
        prev_lower, prev_upper = new_ranges[-1]

        if prev_lower <= lower <= upper <= prev_upper:
            new_ranges[-1] = (min(lower, prev_lower), max(upper, prev_upper))
        elif lower <= prev_upper:
            new_ranges[-1] = (prev_lower, upper)
        else:
            new_ranges.append((lower, upper))

    for lower, upper in new_ranges:
        fresh_ids += upper - lower + 1

    return fresh_ids
