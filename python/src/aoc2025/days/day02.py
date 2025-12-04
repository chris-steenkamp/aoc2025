"""Day 02: [Title]

https://adventofcode.com/2025/day/2
"""

import math


def is_valid_string(x: int) -> bool:
    x: str = str(x)
    length = len(x)
    if length % 2 == 1:
        return True

    return x[: length // 2] != x[length // 2 :]


def is_valid_int(x: int) -> bool:
    num_digits = math.floor(math.log10(x) + 1)

    if num_digits % 2 == 1:
        return True

    half = 10 ** (num_digits // 2)
    return (x // half) != (x % half)


def part_2_naive(input: str) -> bool:
    length = len(input)

    if length < 2:
        return True

    partition_size = 1

    while partition_size <= length // 2:
        if length % partition_size == 0:
            chunk = input[:partition_size]

            if chunk * (length // partition_size) == input:
                return False

        partition_size += 1

    return True


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = input_text.strip().split("\n")

    ids = lines[0].split(",")

    total = 0

    for id in ids:
        lower, upper = id.split("-")
        for i in range(int(lower), int(upper) + 1):
            valid = is_valid_int(i)
            if not valid:
                total += i
    return total


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    ids = lines[0].split(",")

    total = 0

    for id in ids:
        lower, upper = id.split("-")
        for i in range(int(lower), int(upper) + 1):
            valid = part_2_naive(str(i))
            if not valid:
                total += i
    return total
