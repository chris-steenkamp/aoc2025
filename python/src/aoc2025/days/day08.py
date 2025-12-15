"""Day 08: [Title]

https://adventofcode.com/2025/day/8
"""

import heapq
from collections import Counter, defaultdict
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
        for p2 in lines[i + 1 :]:
            heapq.heappush(distances, (euclidean_difference(p, p2), p, p2))

    connections = defaultdict(int)
    circuits = defaultdict(set)
    circuit_num = 0

    for i in range(size):
        _, p1, p2 = heapq.heappop(distances)
        p1_circuit = connections[p1]
        p2_circuit = connections[p2]

        if p1_circuit == p2_circuit == 0:
            circuit_num += 1
            new_circuit = circuit_num
            circuits[new_circuit].add(p1)
            circuits[new_circuit].add(p2)
        elif p1_circuit == 0:
            new_circuit = p2_circuit
            circuits[new_circuit].add(p1)
        elif p2_circuit == 0:
            new_circuit = p1_circuit
            circuits[new_circuit].add(p2)
        elif p1_circuit != p2_circuit:
            new_circuit = p1_circuit
            for c in circuits[p2_circuit]:
                connections[c] = new_circuit

            circuits[new_circuit] |= circuits[p2_circuit]
            del circuits[p2_circuit]
        else:
            continue

        connections[p1] = new_circuit
        connections[p2] = new_circuit

    totals = Counter(connections.values())

    return prod(map(lambda x: x[1], totals.most_common(3)))


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = map(parse_numbers, input_text.strip().split("\n"))
    lines = list(map(lambda x: Point3(x), lines))

    distances = []
    junction_boxes = set(lines)

    for i, p1 in enumerate(lines):
        for p2 in lines[i + 1 :]:
            heapq.heappush(distances, (euclidean_difference(p1, p2), p1, p2))

    while len(junction_boxes) > 0:
        _, p1, p2 = heapq.heappop(distances)

        total = p1[0] * p2[0]

        if p1 in junction_boxes:
            junction_boxes.remove(p1)

        if p2 in junction_boxes:
            junction_boxes.remove(p2)

    return total
