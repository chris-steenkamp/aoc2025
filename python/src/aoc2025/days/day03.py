"""Day 03: [Title]

https://adventofcode.com/2025/day/3
"""


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = input_text.strip().split("\n")
    sum = 0

    for line in lines:
        l = 0
        max_l = 0
        max_r = 0

        for i, c in enumerate(line[:-1]):
            if int(c) > max_l:
                max_l = int(c)
                l = i

        for c in line[l + 1 :]:
            if int(c) > max_r:
                max_r = int(c)

        sum += int(f"{max_l}{max_r}")

    return sum


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    sum = 0

    for line in lines:
        current_pos = 0
        num_batteries = 12
        length = len(line)
        max_vals = [0] * num_batteries
        max_pos = [0] * num_batteries

        for x in range(num_batteries):
            for i, c in enumerate(line[current_pos : length - (num_batteries - x - 1)]):
                if int(c) > max_vals[x]:
                    max_vals[x] = int(c)
                    max_pos[x] = current_pos + i
            current_pos = max_pos[x] + 1

        digits = "".join((str(c) for c in max_vals))
        sum += int(digits)
        print(digits)

    return sum
