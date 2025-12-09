"""Direction and coordinate utilities.

Common types for working with 2D and 3D positions and directions.
"""

import math
from enum import Enum

# Type alias for a 2D point
Point = tuple[int, int]

# Type alias for a 3D point
Point3 = tuple[int, int, int]


class Direction(Enum):
    """Cardinal directions."""

    NORTH = (0, -1)
    SOUTH = (0, 1)
    EAST = (1, 0)
    WEST = (-1, 0)

    @classmethod
    def all(cls) -> list["Direction"]:
        """Get all four cardinal directions."""
        return [cls.NORTH, cls.SOUTH, cls.EAST, cls.WEST]

    @property
    def delta(self) -> tuple[int, int]:
        """Get the (dx, dy) delta for this direction."""
        return self.value

    def turn_left(self) -> "Direction":
        """Turn left (counter-clockwise)."""
        turns = {
            Direction.NORTH: Direction.WEST,
            Direction.WEST: Direction.SOUTH,
            Direction.SOUTH: Direction.EAST,
            Direction.EAST: Direction.NORTH,
        }
        return turns[self]

    def turn_right(self) -> "Direction":
        """Turn right (clockwise)."""
        turns = {
            Direction.NORTH: Direction.EAST,
            Direction.EAST: Direction.SOUTH,
            Direction.SOUTH: Direction.WEST,
            Direction.WEST: Direction.NORTH,
        }
        return turns[self]

    def turn_around(self) -> "Direction":
        """Turn around (180 degrees)."""
        turns = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST: Direction.WEST,
            Direction.WEST: Direction.EAST,
        }
        return turns[self]

    @classmethod
    def from_char(cls, c: str) -> "Direction | None":
        """Parse from a character (^, v, <, >, N, S, E, W)."""
        mapping = {
            "^": cls.NORTH,
            "N": cls.NORTH,
            "n": cls.NORTH,
            "U": cls.NORTH,
            "u": cls.NORTH,
            "v": cls.SOUTH,
            "V": cls.SOUTH,
            "S": cls.SOUTH,
            "s": cls.SOUTH,
            "D": cls.SOUTH,
            "d": cls.SOUTH,
            ">": cls.EAST,
            "E": cls.EAST,
            "e": cls.EAST,
            "R": cls.EAST,
            "r": cls.EAST,
            "<": cls.WEST,
            "W": cls.WEST,
            "w": cls.WEST,
            "L": cls.WEST,
            "l": cls.WEST,
        }
        return mapping.get(c)

    def to_char(self) -> str:
        """Convert to a character representation."""
        chars = {
            Direction.NORTH: "^",
            Direction.SOUTH: "v",
            Direction.EAST: ">",
            Direction.WEST: "<",
        }
        return chars[self]


def move_point(point: Point, direction: Direction, distance: int = 1) -> Point:
    """Move a point in a direction by a given distance."""
    dx, dy = direction.delta
    return (point[0] + dx * distance, point[1] + dy * distance)


def manhattan_distance(a: Point, b: Point) -> int:
    """Calculate Manhattan distance between two points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_difference(a: Point3, b: Point3) -> float:
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)
