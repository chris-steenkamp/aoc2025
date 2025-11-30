# 🎄 Advent of Code 2025

Solutions for [Advent of Code 2025](https://adventofcode.com/2025) implemented in **Rust** (learning) and **Python** (familiar).

## 📁 Project Structure

```
aoc2025/
├── .github/
│   └── copilot-instructions.md  # Architecture decisions for AI assistants
├── data/
│   ├── inputs/                   # Puzzle inputs (gitignored - DO NOT COMMIT)
│   └── examples/                 # Example inputs from puzzle descriptions
├── rust/                         # Rust solutions
│   ├── Cargo.toml
│   └── src/
│       ├── main.rs              # CLI entry point
│       ├── lib.rs               # Library exports
│       ├── input.rs             # Input downloading
│       ├── scaffold.rs          # Day scaffolding
│       ├── days/                # Day solutions
│       │   ├── mod.rs
│       │   └── day01.rs
│       └── utils/               # Utility modules
│           ├── mod.rs
│           ├── grid.rs          # 2D grid utilities
│           ├── direction.rs     # Direction/coordinate types
│           ├── parsing.rs       # Input parsing helpers
│           └── pathfinding.rs   # Graph algorithms
├── python/                       # Python solutions
│   ├── pyproject.toml
│   ├── src/aoc2025/
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── cli.py               # CLI entry point
│   │   ├── input.py             # Input downloading
│   │   ├── scaffold.py          # Day scaffolding
│   │   ├── days/                # Day solutions
│   │   │   ├── __init__.py
│   │   │   └── day01.py
│   │   └── utils/               # Utility modules
│   │       ├── __init__.py
│   │       ├── grid.py
│   │       ├── direction.py
│   │       ├── parsing.py
│   │       └── pathfinding.py
│   └── tests/
│       ├── conftest.py
│       └── test_day01.py
├── .gitignore
└── README.md
```

## 🔧 Prerequisites

### Windows (Native - Recommended)

Both Rust and Python have excellent Windows support. No WSL required!

- **Rust**: Install via [rustup](https://rustup.rs/)

  ```powershell
  winget install Rustlang.Rustup
  ```

- **Python 3.12+**: Install via [uv](https://docs.astral.sh/uv/)
  ```powershell
  winget install astral-sh.uv
  ```

### WSL (Alternative)

If you prefer Unix tools, WSL works fine. The project structure is the same.

## 🚀 Setup

### 1. Clone the Repository

```powershell
git clone https://github.com/yourusername/aoc2025.git
cd aoc2025
```

### 2. Set Up Session Cookie

To download puzzle inputs, you need your AoC session cookie:

1. Log in to [adventofcode.com](https://adventofcode.com)
2. Open browser DevTools (F12) → Application → Cookies → adventofcode.com
3. Copy the `session` cookie value

Set the environment variable:

```powershell
# PowerShell (current session)
$env:AOC_SESSION = "your_session_cookie_value_here"

# Or add to your PowerShell profile for persistence
Add-Content $PROFILE '$env:AOC_SESSION = "your_session_cookie_value_here"'
```

Alternatively, create a `.env` file in the project root:

```env
AOC_SESSION=your_session_cookie_value_here
```

### 3. Build/Install

**Rust:**

```powershell
cd rust
cargo build --release
```

**Python:**

```powershell
cd python
uv sync
```

## 📖 Usage

### Running Solutions

**Rust:**

```powershell
cd rust

# Run a specific day (both parts)
cargo run --release -- solve 1

# Run a specific part
cargo run --release -- solve 1 --part 1
cargo run --release -- solve 1 --part 2
```

**Python:**

```powershell
cd python

# Run a specific day (both parts)
uv run aoc solve 1

# Run a specific part
uv run aoc solve 1 --part 1
uv run aoc solve 1 --part 2
```

### Downloading Input

Inputs are auto-downloaded when you run a solution, but you can also download manually:

**Rust:**

```powershell
cd rust
cargo run -- download 1
```

**Python:**

```powershell
cd python
uv run aoc download 1
```

### Scaffolding a New Day

When a new day's puzzle is released:

**Rust:**

```powershell
cd rust
cargo run -- new 2
```

This creates:

- `src/days/day02.rs` (solution template)
- `../data/examples/02.txt` (example input placeholder)

Then manually add to `src/days/mod.rs`:

```rust
pub mod day02;
// And add the match arm in run_day()
```

**Python:**

```powershell
cd python
uv run aoc new 2
```

This creates:

- `src/aoc2025/days/day02.py` (solution template)
- `tests/test_day02.py` (test template)
- `../data/examples/02.txt` (example input placeholder)

Then manually add to `src/aoc2025/days/__init__.py`:

```python
from . import day02
DAYS = {
    1: day01,
    2: day02,  # Add this
}
```

### Running Tests

**Rust:**

```powershell
cd rust

# Run all tests
cargo test

# Run tests for a specific day
cargo test day01

# Run with output
cargo test -- --nocapture
```

**Python:**

```powershell
cd python

# Run all tests
uv run pytest

# Run tests for a specific day
uv run pytest tests/test_day01.py

# Run with verbose output
uv run pytest -v
```

## 🗓️ Daily Workflow

1. **Wait for puzzle release** (midnight EST / 05:00 UTC)

2. **Read the puzzle** at `https://adventofcode.com/2025/day/N`

3. **Scaffold the day:**

   ```powershell
   cd rust && cargo run -- new N
   # or
   cd python && uv run aoc new N
   ```

4. **Copy the example input** from the puzzle page into `data/examples/NN.txt`

5. **Update the test** with expected values from the puzzle

6. **Implement Part 1**, run tests until they pass:

   ```powershell
   cargo test day0N
   # or
   uv run pytest tests/test_day0N.py
   ```

7. **Run with real input:**

   ```powershell
   cargo run --release -- solve N --part 1
   # or
   uv run aoc solve N --part 1
   ```

8. **Submit answer** on the website

9. **Repeat for Part 2**

## 🛠️ Utility Modules

Both languages provide scaffolded utility modules:

### Grid (`utils/grid`)

- 2D grid data structure
- `get(x, y)`, `set(x, y, value)`
- `neighbors(x, y)` - 4 cardinal directions
- `neighbors_diagonal(x, y)` - 8 directions
- `find(value)` - locate first occurrence

### Direction (`utils/direction`)

- `Direction` enum (North, South, East, West)
- `Point` type alias
- `turn_left()`, `turn_right()`, `turn_around()`
- `manhattan_distance(a, b)`

### Parsing (`utils/parsing`)

- `parse_numbers(text)` - extract all integers
- `parse_grid(text)` - 2D character grid
- `parse_lines(text)` - non-empty lines
- `parse_groups(text)` - sections separated by blank lines

### Pathfinding (`utils/pathfinding`)

- `bfs` - Breadth-first search (unweighted)
- `dijkstra` - Weighted shortest path
- `astar` - A\* with heuristic
- `flood_fill` - Find all reachable nodes

## 📊 Progress

| Day | Part 1 | Part 2 | Rust | Python | Notes |
| --- | ------ | ------ | ---- | ------ | ----- |
| 01  | ⬜     | ⬜     | ⬜   | ⬜     |       |
| 02  | ⬜     | ⬜     | ⬜   | ⬜     |       |
| ... | ...    | ...    | ...  | ...    |       |
| 25  | ⬜     | ⬜     | ⬜   | ⬜     |       |

⬜ Not started | 🟡 In progress | ✅ Complete

## 🏗️ Architecture Decisions

See [`.github/copilot-instructions.md`](.github/copilot-instructions.md) for detailed architecture decisions and conventions.

Key decisions:

- **Dual language support**: Rust for learning, Python as fallback
- **Shared data directory**: Both languages use `../data/` for inputs/examples
- **Simple dispatch**: `match` in Rust, dict in Python (no macros/magic)
- **Auto-download**: Inputs downloaded automatically if missing
- **Timing output**: All solutions display elapsed time in milliseconds
- **Stable Rust**: Edition 2021 for reliability while learning

## ⚠️ Important Notes

- **DO NOT COMMIT** puzzle inputs (`data/inputs/`) - they are unique to each user
- Example inputs (`data/examples/`) CAN be committed - they're from puzzle descriptions
- Session cookies expire ~monthly - refresh if downloads fail
- Respect AoC's servers - don't spam requests

## 📜 License

This project is for personal educational use for Advent of Code 2025.

Puzzle content copyright [Advent of Code](https://adventofcode.com) / Eric Wastl.
