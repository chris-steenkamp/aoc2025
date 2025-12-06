"""Grid utilities for 2D puzzle grids.

Provides a Grid class for working with 2D arrays.
"""

from typing import Callable, Generic, Iterator, TypeVar

T = TypeVar("T")


class Grid(Generic[T]):
    """A 2D grid of values."""

    def __init__(self, data: list[list[T]]):
        """Create a grid from a 2D list.

        Args:
            data: 2D list where data[y][x] is the value at position (x, y)
        """
        self.data = data
        self.height = len(data)
        self.width = len(data[0]) if data else 0

    @classmethod
    def from_string(cls, input_text: str) -> "Grid[str]":
        """Parse a grid from a multi-line string.

        Each character becomes a cell.
        """
        data = [list(line) for line in input_text.strip().split("\n")]
        return cls(data)

    @classmethod
    def filled(cls, width: int, height: int, value: T) -> "Grid[T]":
        """Create a grid filled with a default value."""
        data = [[value for _ in range(width)] for _ in range(height)]
        return cls(data)

    def get(self, x: int, y: int) -> T | None:
        """Get the value at (x, y), or None if out of bounds."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.data[y][x]
        return None

    def set(self, x: int, y: int, value: T) -> bool:
        """Set the value at (x, y). Returns True if successful."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.data[y][x] = value
            return True
        return False

    def neighbors(self, x: int, y: int) -> list[tuple[int, int]]:
        """Get the 4 cardinal neighbors (N, S, E, W) of a position."""
        result = []
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                result.append((nx, ny))
        return result

    def neighbors_diagonal(self, x: int, y: int) -> list[tuple[int, int]]:
        """Get all 8 neighbors including diagonals."""
        result = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    result.append((nx, ny))
        return result

    def iter(self) -> Iterator[tuple[tuple[int, int], T]]:
        """Iterate over all positions and values."""
        for y in range(self.height):
            for x in range(self.width):
                yield (x, y), self.data[y][x]

    def find(self, value: T) -> tuple[int, int] | None:
        """Find the first position with the given value."""
        for (x, y), v in self.iter():
            if v == value:
                return (x, y)
        return None

    def find_all(self, value: T) -> list[tuple[int, int]]:
        """Find all positions with the given value."""
        return [(x, y) for (x, y), v in self.iter() if v == value]

    def find_where(self, predicate: Callable[[T], bool]) -> tuple[int, int] | None:
        """Find the first position where predicate returns True."""
        for (x, y), v in self.iter():
            if predicate(v):
                return (x, y)
        return None

    def rotate_right(self) -> "Grid[T]":
        """Rotate the grid 90 degrees clockwise.

        Returns a new Grid with the rotation applied.
        """
        new_data = [
            [self.data[self.height - 1 - y][x] for y in range(self.height)]
            for x in range(self.width)
        ]
        return Grid(new_data)

    def rotate_left(self) -> "Grid[T]":
        """Rotate the grid 90 degrees counter-clockwise.

        Returns a new Grid with the rotation applied.
        """
        new_data = [
            [self.data[y][self.width - 1 - x] for y in range(self.height)]
            for x in range(self.width)
        ]
        return Grid(new_data)

    def row(self, y: int) -> list[T] | None:
        """Get an entire row by index.

        Args:
            y: The row index (0-indexed from top)

        Returns:
            A copy of the row as a list, or None if out of bounds.
        """
        if 0 <= y < self.height:
            return self.data[y][:]
        return None

    def __str__(self) -> str:
        """Convert grid to string for display."""
        return "\n".join("".join(str(cell) for cell in row) for row in self.data)

    def __repr__(self) -> str:
        return f"Grid({self.width}x{self.height})"
