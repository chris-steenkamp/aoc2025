"""Day 11: [Title]

https://adventofcode.com/2025/day/11
"""

from collections import deque


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


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
