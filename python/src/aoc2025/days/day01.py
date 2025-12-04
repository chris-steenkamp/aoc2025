"""Day 01: [Title]

https://adventofcode.com/2025/day/1
"""


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = input_text.strip().split("\n")

    total = 50
    size = 100
    zeroes = 0

    for l in lines:
        print(
            f"Line: {l} Total {total} should change by {(int(l[1:]) * (1 if l[0] == 'R' else -1))}"
        )
        total += int(l[1:]) * (1 if l[0] == "R" else -1)
        total %= size
        zeroes += 1 if total == 0 else 0

    return zeroes


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    size = 100
    total = 50
    zeroes = 0

    for line in lines:
        direction = 1 if line[0] == "R" else -1

        delta = int(line[1:])

        print(f"Line: {line} Total {total} should change by {delta}", end="")

        clicks = delta // size
        delta = delta % size

        if clicks > 0:
            print(f" (intermediate clicks: {clicks})", end="")

        if delta > 0:
            new_total = total + direction * delta
            if (direction == 1 and new_total >= size) or (
                direction == -1 and new_total < 1 and total != 0
            ):
                zeroes += 1
                print(" (hit zero!)", end="")
            total = new_total % size

        zeroes += clicks
        print(f" new total: {total}), total zeroes: {zeroes}")

    return zeroes


def part_two2(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    total = 50
    size = 100
    zeroes = 0

    for l in lines:
        clicks = 0
        delta = int(l[1:]) * (1 if l[0] == "R" else -1)
        print(f"Line: {l} Total {total} should change by {delta}", end="")
        if delta < 0 and abs(delta) > total:
            clicks = (abs(delta) - total - 1) // size + 1
        elif delta > 0 and delta > (size - total):
            clicks = (delta - (size - total) - 1) // size
            # clicks = (delta - total) // size + 1
        else:
            clicks = 0

        if clicks > 0:
            print(f" (intermediate clicks: {clicks})", end="")

        total += delta
        total %= size
        zeroes += 1 if total == 0 else 0
        if total == 0:
            print(" (hit zero!)", end="")
        zeroes += clicks
        print(f" new total: {total}), total zeroes: {zeroes}")

    return zeroes
