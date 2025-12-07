"""Day 07: [Title]

https://adventofcode.com/2025/day/7
"""

import heapq

from aoc2025.utils.grid import Grid


def check_and_add(splitter_x, splitter_y, valid_splitters):
    # uses a heap with negative values to simulate a max heap
    # this allows us to find the most recently encountered splitter
    # for a given x postition.
    if splitter_x not in valid_splitters:
        valid_splitters[splitter_x] = [-splitter_y]
        return True

    most_recent_x = -valid_splitters[splitter_x][0]
    if splitter_y > most_recent_x:
        for y in range(most_recent_x, splitter_y):
            # Chek if there is a reachable splitter between the current splitter
            # and the most recent splitter at the same x position. If not, then
            # there is no way for the beam to enter the current splitter and thus
            # no beam will be split.
            if (
                -valid_splitters[splitter_x - 1][0] == y
                or -valid_splitters[splitter_x + 1][0] == y
            ):
                heapq.heappush(valid_splitters[splitter_x], -splitter_y)
                return True

        return False

    return False


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    grid = Grid.from_string(input_text)
    splitters = grid.find_all("^")

    valid_beam_splitters = {}

    splitters = filter(
        lambda x: check_and_add(x[0], x[1], valid_beam_splitters), splitters
    )

    return len(list(splitters))


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
