"""Day 07: [Title]

https://adventofcode.com/2025/day/7
"""

import bisect
import heapq
from collections import defaultdict

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
    grid = Grid.from_string(input_text)
    splitters = grid.find_all("^")

    valid_beam_splitters = {}

    # Filter to get reachable splitters (already ordered by y, then x)
    splitters = list(
        filter(lambda x: check_and_add(x[0], x[1], valid_beam_splitters), splitters)
    )

    # Build index: map x -> list of (y, index in splitters list)
    # This preserves ordering while allowing O(log n) lookups
    splitters_by_x = defaultdict(list)
    for idx, (x, y) in enumerate(splitters):
        splitters_by_x[x].append((y, idx))

    def find_next_splitter(target_x, current_y):
        """Binary search for the next splitter at target_x with y > current_y."""
        if target_x not in splitters_by_x:
            return None

        # Binary search for first y > current_y
        candidates = splitters_by_x[target_x]
        idx = bisect.bisect_right(candidates, (current_y, float("inf")))

        if idx < len(candidates):
            y, splitter_idx = candidates[idx]
            return splitter_idx

        return None

    # Memoization cache: splitter_idx -> timeline_count
    # No cycles possible since y always increases
    memo = {}

    def count_timelines(splitter_idx):
        """Count timelines - particle takes BOTH paths, creating timeline splits."""
        # Check cache
        if splitter_idx in memo:
            return memo[splitter_idx]

        x, y = splitters[splitter_idx]

        # Find next reachable splitters at x-1 and x+1
        left_idx = find_next_splitter(x - 1, y)
        right_idx = find_next_splitter(x + 1, y)

        # Both paths lead off grid immediately = 2 timelines
        if left_idx is None and right_idx is None:
            result = 2
        # One path has a splitter, other goes off grid
        elif left_idx is None:
            # Left beam exits (1 timeline), right beam continues
            result = 1 + count_timelines(right_idx)
        elif right_idx is None:
            # Right beam exits (1 timeline), left beam continues
            result = 1 + count_timelines(left_idx)
        else:
            # Both paths have splitters - both timelines continue and split further
            left_timelines = count_timelines(left_idx)
            right_timelines = count_timelines(right_idx)
            result = left_timelines + right_timelines

        memo[splitter_idx] = result
        return result

    # Start from the first splitter
    return count_timelines(0)
