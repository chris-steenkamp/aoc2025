"""Day 10: [Title]

https://adventofcode.com/2025/day/10
"""

from collections import deque


def parse_input(input_text):
    lines = input_text.strip().split("\n")
    machines = []
    buttons = []
    button_bits = []
    for line in lines:
        machine, button = line.split(" ", 1)
        button, _ = button.rsplit(" ", 1)

        machines.append(list(map(lambda x: "1" if x == "#" else "0", machine[1:-1])))
        buttons.append([tuple(map(int, i[1:-1].split(","))) for i in button.split(" ")])
        sequences = []
        for machine_button_sequence in buttons[-1]:
            bit_string = ["0"] * len(machines[-1])
            for button_sequence in machine_button_sequence:
                bit_string[button_sequence] = "1"
            sequences.append(int("".join(bit_string), 2))
        button_bits.append(sequences)
    return machines, button_bits


def bfs(start, goal, options, max_depth=5):
    queue = deque([(start, 0, [start], 0)])
    visited = set()
    shortest_solution_length = float("inf")
    shortest_solution_path = []

    while queue:
        current_op, current_val, current_path, current_depth = queue.popleft()
        if current_depth >= max_depth or current_depth >= shortest_solution_length:
            continue

        new_val = current_val ^ current_op

        state = (new_val, current_depth)

        if state in visited:
            continue

        visited.add(state)

        if goal == new_val:
            solution_length = len(current_path)
            if solution_length < shortest_solution_length:
                shortest_solution_length = solution_length
                shortest_solution_path = current_path
            continue

        for next_op in options:
            if next_op == current_op:
                # xoring the same value twice in a row results in 0
                # which is a noop and can never be the fastest way
                # to toggle the lights (it always adds 2 unnecessary steps)
                continue

            new_path = current_path + [next_op]
            queue.append((next_op, new_val, new_path, current_depth + 1))

    return shortest_solution_path


def part_one(input_text: str) -> int | None:
    """Solve part one."""
    machines, button_sequences = parse_input(input_text)

    solutions = {}

    for i, machine in enumerate(machines):
        goal = int("".join(machine), 2)
        shortest_solution_length = float("inf")
        for seq in button_sequences[i]:
            shortest_solution_path = bfs(seq, goal, button_sequences[i], max_depth=100)
            if len(shortest_solution_path) < shortest_solution_length:
                solutions[i] = shortest_solution_path
                shortest_solution_length = len(shortest_solution_path)

    return sum((len(s) for s in solutions.values()))


def part_two(input_text: str) -> int | None:
    """Solve part two."""
    lines = input_text.strip().split("\n")

    # TODO: Implement solution
    return None
