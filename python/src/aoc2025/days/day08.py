"""Day 08: [Title]

https://adventofcode.com/2025/day/8
"""

import heapq
from collections import defaultdict, deque
from math import prod

from aoc2025.utils.direction import Point3, euclidean_difference
from aoc2025.utils.parsing import parse_numbers


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    lines = map(parse_numbers, input_text.strip().split("\n"))
    lines = list(map(lambda x: Point3(x), lines))
    size = 10 if len(lines) < 21 else 1000

    distances = []
    for i, p in enumerate(lines):
        for p2 in lines[i:]:
            if p != p2:
                heapq.heappush(distances, (euclidean_difference(p, p2), p, p2))

    circuits = defaultdict(set)
    for i in range(size):
        _, p1, p2 = heapq.heappop(distances)
        circuits[p1].add(p2)
        circuits[p2].add(p1)

    visited = []
    keys = list(circuits.keys())

    for i in range(len(keys)):
        visited.append(set())
        start = keys[i]

        v = deque([start])
        while len(v):
            current = v.popleft()
            visited[i].add(current)
            for n in circuits[current]:
                if n not in visited[i]:
                    v.append(n)

    circuits = sorted(
        [len(s) for s in set(frozenset(v) for v in visited)], reverse=True
    )
    return prod(circuits[:3])


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
