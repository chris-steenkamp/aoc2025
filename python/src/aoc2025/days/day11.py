"""Day 11: [Title]

https://adventofcode.com/2025/day/11
"""

from collections import deque
from functools import cache


def bfs(start, goal, nodes):
    visited = set()
    queue = deque([(start, [start])])
    solutions = []

    while queue:
        current_node, current_path = queue.popleft()

        if current_node == goal:
            solutions.append(current_path)
            continue

        for next_node in nodes[current_node]:
            queue.append((next_node, current_path + [next_node]))

    return solutions


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = input_text.strip().split("\n")
    graph = {k[:-1]: v for k, *v in [line.split(" ") for line in lines]}
    solutions = bfs("you", "out", graph)

    return len(solutions)


def count_paths(start, goal, nodes, must_visit=frozenset()):
    @cache
    def count_from(node, remaining):
        if node == goal:
            return 1 if len(remaining) == 0 else 0

        if node not in nodes:
            return 0

        new_remaining = remaining - {node}

        total = 0
        for next_node in nodes[node]:
            total += count_from(next_node, new_remaining)

        return total

    return count_from(start, must_visit)


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")
    graph = {k[:-1]: v for k, *v in [line.split(" ") for line in lines]}

    count = count_paths("svr", "out", graph, frozenset(["dac", "fft"]))

    return count
