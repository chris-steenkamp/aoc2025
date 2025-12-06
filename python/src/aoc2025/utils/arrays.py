"""Array utilities for 2D array manipulation.

Provides standalone functions for working with 2D lists/arrays.
"""

from typing import TypeVar

T = TypeVar("T")


def rotate_right(array: list[list[T]]) -> list[list[T]]:
    """Rotate a 2D array 90 degrees clockwise.

    Args:
        array: A 2D list where array[y][x] is the value at row y, column x

    Returns:
        A new 2D list with the rotation applied.
        The new dimensions are (original_width x original_height).

    Example:
        >>> rotate_right([[1, 2, 3], [4, 5, 6]])
        [[4, 1], [5, 2], [6, 3]]
    """
    if not array or not array[0]:
        return []
    height = len(array)
    width = len(array[0])
    return [[array[height - 1 - y][x] for y in range(height)] for x in range(width)]


def rotate_left(array: list[list[T]]) -> list[list[T]]:
    """Rotate a 2D array 90 degrees counter-clockwise.

    Args:
        array: A 2D list where array[y][x] is the value at row y, column x

    Returns:
        A new 2D list with the rotation applied.
        The new dimensions are (original_width x original_height).

    Example:
        >>> rotate_left([[1, 2, 3], [4, 5, 6]])
        [[3, 6], [2, 5], [1, 4]]
    """
    if not array or not array[0]:
        return []
    height = len(array)
    width = len(array[0])
    return [[array[y][width - 1 - x] for y in range(height)] for x in range(width)]


def rotate_180(array: list[list[T]]) -> list[list[T]]:
    """Rotate a 2D array 180 degrees.

    Args:
        array: A 2D list where array[y][x] is the value at row y, column x

    Returns:
        A new 2D list with the rotation applied.
        The dimensions remain the same.

    Example:
        >>> rotate_180([[1, 2, 3], [4, 5, 6]])
        [[6, 5, 4], [3, 2, 1]]
    """
    if not array or not array[0]:
        return []
    return [row[::-1] for row in array[::-1]]


def transpose(array: list[list[T]]) -> list[list[T]]:
    """Transpose a 2D array (swap rows and columns).

    Args:
        array: A 2D list where array[y][x] is the value at row y, column x

    Returns:
        A new 2D list where result[x][y] = array[y][x].

    Example:
        >>> transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    if not array or not array[0]:
        return []
    return [list(row) for row in zip(*array)]
