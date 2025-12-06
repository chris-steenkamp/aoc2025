"""Day solution modules.

Each day is implemented as a separate module (day01, day02, etc.).
"""

from . import day01, day02, day03, day04, day05, day06

# Dictionary mapping day numbers to modules
DAYS = {1: day01, 2: day02, 3: day03, 4: day04, 5: day05, 6: day06}


def run_day(day: int, part: int, input_text: str) -> int | None:
    """Run a specific day and part, returning the result.

    Args:
        day: Day number (1-25)
        part: Part number (1 or 2)
        input_text: The puzzle input as a string

    Returns:
        The answer if the solution is implemented, None otherwise.
    """
    if day not in DAYS:
        print(f"Day {day} is not implemented yet")
        return None

    module = DAYS[day]

    if part == 1:
        return module.part_one(input_text)
    elif part == 2:
        return module.part_two(input_text)
    else:
        return None
