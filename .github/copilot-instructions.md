# Advent of Code 2025 - Architecture & Conventions

This document captures architectural decisions and conventions for the AoC 2025 project. AI assistants and future contributors should follow these guidelines for consistency.

## Project Context

- **Year**: 2025 (puzzles release December 1-25)
- **Primary Language**: Rust (learning this year)
- **Secondary Language**: Python (comfortable fallback)
- **Development Environment**: Windows (native, no WSL required)
- **Python Tooling**: Always use `uv` (never raw `pip` or `python`)

## Key Architecture Decisions

### 1. Platform: Native Windows

**Decision**: Run both Rust and Python natively on Windows.

**Rationale**:
- Rust has excellent Windows support via `rustup`
- Python works well via `uv`
- WSL adds unnecessary complexity
- All tooling (cargo, uv) works identically on Windows

**Fallback**: WSL is available if native builds encounter issues.

### 2. Rust Edition: 2021

**Decision**: Use Rust edition 2021 (not 2024).

**Rationale**:
- 2021 is stable and well-documented
- Avoiding bleeding-edge changes while learning
- Better IDE support and error messages
- Most tutorials and examples use 2021

### 3. Rust TLS: rustls

**Decision**: Use `rustls-tls` feature for `reqwest` (not `native-tls`).

**Rationale**:
- Pure Rust implementation
- No OpenSSL dependency on Windows
- Simpler builds, fewer system dependencies

### 4. Directory Layout: Side-by-Side with Shared Data

**Decision**: Separate `rust/` and `python/` directories with shared `data/` at root.

```
aoc2025/
├── data/           # Shared between languages
│   ├── inputs/     # Real inputs (gitignored)
│   └── examples/   # Sample inputs (committed)
├── rust/           # Rust project
└── python/         # Python project
```

**Rationale**:
- Clean separation of language ecosystems
- Single source of truth for inputs
- Easy to work in one language without touching the other
- Both reference `../data/` via relative paths

### 5. File Naming Convention

**Decision**: Zero-padded two-digit format.

- Day modules: `day01.rs`, `day01.py`
- Input files: `01.txt`, `02.txt`
- Test files: `test_day01.py`

**Rationale**:
- Consistent sorting in file explorers
- Clear visual alignment
- Matches common AoC conventions

### 6. Module Function Signatures

**Rust**:
```rust
pub fn part_one(input: &str) -> Option<u64>
pub fn part_two(input: &str) -> Option<u64>
```

**Python**:
```python
def part_one(input_text: str) -> int | None
def part_two(input_text: str) -> int | None
```

**Rationale**:
- `Option`/`None` return allows "not implemented yet" state
- Distinguishes "no answer" from "answer is zero"
- String input is flexible for any puzzle format
- `u64`/`int` covers most AoC answers (some may need adjustment)

### 7. Day Dispatch Pattern

**Rust**: Simple `match` statement in `days/mod.rs`

```rust
match day {
    1 => match part {
        1 => day01::part_one(input).map(|v| v as i64),
        2 => day01::part_two(input).map(|v| v as i64),
        _ => None,
    },
    // Add new days here
    _ => None,
}
```

**Python**: Dict mapping in `days/__init__.py`

```python
DAYS = {
    1: day01,
    2: day02,
    # Add new days here
}

module = DAYS.get(day)
if module:
    if part == 1:
        return module.part_one(input_text)
```

**Rationale**:
- Explicit over implicit (no macro magic)
- Easy to understand for Rust beginners
- Simple to add new days
- Clear error when day not implemented

### 8. Template Embedding

**Decision**: Embed day/test templates as string constants in scaffold modules.

**Rationale**:
- Single source of truth
- No separate template files to maintain
- Changes to template immediately affect scaffolding
- Simpler project structure

### 9. Testing Strategy

**Example Inputs** (`data/examples/`):
- Committed to git
- Copied from puzzle descriptions
- Used in unit tests
- Safe to share

**Real Inputs** (`data/inputs/`):
- Gitignored (NEVER commit)
- Unique per user
- Downloaded via session cookie
- Used for actual solutions

**Test Structure**:
- Each day has tests for both parts
- Tests use example input by default
- Expected values come from puzzle description
- Tests start as `assert result is None` until implemented

### 10. Input Handling

**Auto-download**: When running a solution, if input doesn't exist, download it automatically.

**Environment Variable**: `AOC_SESSION` contains the session cookie value (just the value, not `session=`).

**User-Agent**: Include contact info in HTTP requests to be a good citizen.

**Storage**: Save to `data/inputs/{day:02d}.txt`

### 11. CLI Design

**Subcommand Pattern**:
- `solve <day> [--part <1|2>]` - Run solution with timing
- `download <day>` - Fetch input
- `new <day>` - Scaffold new day

**Output Format**:
```
🎄 Advent of Code 2025 - Day 01
========================================
Part 1: 12345
  ⏱️  1.234ms

Part 2: 67890
  ⏱️  5.678ms
```

### 12. Timing

**Decision**: Always display elapsed time in milliseconds.

**Implementation**:
- Rust: `std::time::Instant`
- Python: `time.perf_counter()`

**Format**: `⏱️  X.XXXms` (3 decimal places)

### 13. Code Style

**Rust**:
- Follow `rustfmt` defaults
- Use `cargo fmt` before committing
- Prefer explicit types while learning

**Python**:
- Follow PEP 8
- Use type hints (Python 3.12+ syntax: `int | None`)
- Use `ruff` if available

## Conventions for Adding New Days

### Rust

1. Run `cargo run -- new N`
2. Edit `data/examples/NN.txt` with sample input
3. Add to `src/days/mod.rs`:
   - `pub mod dayNN;`
   - Match arm in `run_day()`
4. Implement solution in `src/days/dayNN.rs`
5. Update test expected values
6. Run `cargo test dayNN`

### Python

1. Run `uv run aoc new N`
2. Edit `data/examples/NN.txt` with sample input
3. Add to `src/aoc2025/days/__init__.py`:
   - `from . import dayNN`
   - Entry in `DAYS` dict
4. Implement solution in `src/aoc2025/days/dayNN.py`
5. Update test expected values in `tests/test_dayNN.py`
6. Run `uv run pytest tests/test_dayNN.py`

## Utility Module Guidelines

### When to Use Utilities

- **Grid**: Any 2D puzzle with a map/board
- **Direction**: Movement puzzles, path following
- **Parsing**: Complex input formats
- **Pathfinding**: Maze solving, shortest path, graph traversal

### Extending Utilities

- Add methods as needed during puzzles
- Keep implementations simple and readable
- Prefer clarity over cleverness (learning context)
- Add tests for complex additions

## Common Patterns

### Reading Input

**Rust**:
```rust
let lines: Vec<&str> = input.lines().collect();
let grid = parse_grid(input);
let numbers = parse_numbers(input);
```

**Python**:
```python
lines = input_text.strip().split("\n")
grid = parse_grid(input_text)
numbers = parse_numbers(input_text)
```

### Grid Navigation

**Rust**:
```rust
use crate::utils::grid::Grid;
use crate::utils::direction::{Direction, Point};

let grid = Grid::from_str(input)?;
let start = grid.find('S')?;

for (nx, ny) in grid.neighbors(x, y) {
    // process neighbor
}
```

**Python**:
```python
from aoc2025.utils import Grid, Direction, Point

grid = Grid.from_string(input_text)
start = grid.find('S')

for nx, ny in grid.neighbors(x, y):
    # process neighbor
```

### BFS Example

**Rust**:
```rust
use crate::utils::pathfinding::bfs;

let path = bfs(
    &start,
    |&pos| grid.neighbors(pos.0, pos.1).into_iter(),
    |&pos| pos == goal,
);
```

**Python**:
```python
from aoc2025.utils import bfs

path = bfs(
    start,
    lambda pos: grid.neighbors(pos[0], pos[1]),
    lambda pos: pos == goal,
)
```

## Troubleshooting

### Session Cookie Expired

Symptoms: HTTP 400 or 500 errors when downloading
Fix: Get fresh cookie from browser, update `AOC_SESSION`

### Input Already Exists

The download command won't overwrite. Delete the file first if needed:
```powershell
Remove-Item data/inputs/01.txt
```

### Rust Compilation Slow

First build downloads/compiles dependencies. Subsequent builds are faster.
Use `cargo run` (debug) for development, `cargo run --release` for timing.

### Python Import Errors

Ensure you're in the `python/` directory and using `uv run`.
Check that `uv sync` completed successfully.

## Contact

For architecture questions or changes, update this document and discuss in PR.
