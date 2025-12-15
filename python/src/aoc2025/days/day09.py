"""Day 09: [Title]

https://adventofcode.com/2025/day/9
"""

import heapq
from collections import deque

from aoc2025.utils.direction import Direction, Point, manhattan_distance
from aoc2025.utils.parsing import parse_unsigned


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    corners = list(
        map(Point, [parse_unsigned(p) for p in input_text.strip().split("\n")])
    )

    distances = []

    for i, p1 in enumerate(corners):
        for p2 in corners[i + 1 :]:
            heapq.heappush(distances, (-manhattan_distance(p1, p2), p1, p2))

    _, p1, p2 = heapq.heappop(distances)

    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


def compress_coordinates(coordinates):
    x_values = [c[0] for c in coordinates]
    y_values = [c[1] for c in coordinates]
    unique_x, unique_y = sorted(set(x_values)), sorted(set(y_values))
    x_rank = {x: i for i, x in enumerate(unique_x)}
    y_rank = {y: i for i, y in enumerate(unique_y)}
    return [(x_rank[x], y_rank[y]) for x, y in coordinates]


def span(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    x_min, x_max = sorted((x1, x2))
    y_min, y_max = sorted((y1, y2))
    return {(x, y) for x in range(x_min, x_max + 1) for y in range(y_min, y_max + 1)}


def create_borders(coordinates):
    borders = set()
    complete = coordinates + [coordinates[0]]
    for c1, c2 in zip(complete, complete[1:]):
        borders |= span(c1, c2)
    return borders


def calculate_area(rectangle):
    (x1, y1), (x2, y2) = rectangle
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def rectangle_inside(p1, p2, polygon):
    x1, y1 = p1
    x2, y2 = p2
    x_min, x_max = sorted((x1, x2))
    y_min, y_max = sorted((y1, y2))
    for x in range(x_min, x_max + 1):
        if (x, y_min) not in polygon or (x, y_max) not in polygon:
            return False
    for y in range(y_min, y_max + 1):
        if (x_min, y) not in polygon or (x_max, y) not in polygon:
            return False
    return True


def flood_fill(start, limits):
    dirs = [d.delta for d in Direction]
    visited = {start}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for dx, dy in dirs:
            p = (current[0] + dx, current[1] + dy)
            if p in limits:
                continue

            if p not in visited:
                visited.add(p)
                queue.append(p)

    return visited


def part_two(input_text: str):
    coordinates = [
        tuple(parse_unsigned(line)) for line in input_text.strip().split("\n")
    ]
    compressed = compress_coordinates(coordinates)
    borders = create_borders(compressed)
    if len(coordinates) == 8:
        start_point = Point([1, 1])
    else:
        start_point = (150, 150)

    interior = flood_fill(start_point, borders)

    polygon = borders | interior
    max_area = 0
    for i, p1 in enumerate(compressed):
        for j, p2 in enumerate(compressed[i + 1 :], i + 1):
            area = calculate_area((coordinates[i], coordinates[j]))
            if area <= max_area:
                continue
            if rectangle_inside(p1, p2, polygon):
                max_area = area
    return max_area
