//! Direction and coordinate utilities
//!
//! Common types for working with 2D positions and directions.

/// A 2D point with signed coordinates
pub type Point = (i32, i32);

/// Cardinal directions
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum Direction {
    North,
    South,
    East,
    West,
}

impl Direction {
    /// Get all four cardinal directions
    pub fn all() -> [Direction; 4] {
        [
            Direction::North,
            Direction::South,
            Direction::East,
            Direction::West,
        ]
    }

    /// Get the (dx, dy) delta for this direction
    /// North is -y, South is +y, West is -x, East is +x
    pub fn delta(&self) -> (i32, i32) {
        match self {
            Direction::North => (0, -1),
            Direction::South => (0, 1),
            Direction::East => (1, 0),
            Direction::West => (-1, 0),
        }
    }

    /// Turn left (counter-clockwise)
    pub fn turn_left(&self) -> Self {
        match self {
            Direction::North => Direction::West,
            Direction::West => Direction::South,
            Direction::South => Direction::East,
            Direction::East => Direction::North,
        }
    }

    /// Turn right (clockwise)
    pub fn turn_right(&self) -> Self {
        match self {
            Direction::North => Direction::East,
            Direction::East => Direction::South,
            Direction::South => Direction::West,
            Direction::West => Direction::North,
        }
    }

    /// Turn around (180 degrees)
    pub fn turn_around(&self) -> Self {
        match self {
            Direction::North => Direction::South,
            Direction::South => Direction::North,
            Direction::East => Direction::West,
            Direction::West => Direction::East,
        }
    }

    /// Parse from a character (^, v, <, >, N, S, E, W)
    pub fn from_char(c: char) -> Option<Self> {
        match c {
            '^' | 'N' | 'n' | 'U' | 'u' => Some(Direction::North),
            'v' | 'V' | 'S' | 's' | 'D' | 'd' => Some(Direction::South),
            '>' | 'E' | 'e' | 'R' | 'r' => Some(Direction::East),
            '<' | 'W' | 'w' | 'L' | 'l' => Some(Direction::West),
            _ => None,
        }
    }

    /// Convert to a character representation
    pub fn to_char(&self) -> char {
        match self {
            Direction::North => '^',
            Direction::South => 'v',
            Direction::East => '>',
            Direction::West => '<',
        }
    }
}

/// Move a point in a direction
pub fn move_point(point: Point, direction: Direction) -> Point {
    let (dx, dy) = direction.delta();
    (point.0 + dx, point.1 + dy)
}

/// Move a point in a direction by a given distance
pub fn move_point_by(point: Point, direction: Direction, distance: i32) -> Point {
    let (dx, dy) = direction.delta();
    (point.0 + dx * distance, point.1 + dy * distance)
}

/// Calculate Manhattan distance between two points
pub fn manhattan_distance(a: Point, b: Point) -> i32 {
    (a.0 - b.0).abs() + (a.1 - b.1).abs()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_direction_turn() {
        assert_eq!(Direction::North.turn_right(), Direction::East);
        assert_eq!(Direction::North.turn_left(), Direction::West);
        assert_eq!(Direction::North.turn_around(), Direction::South);
    }

    #[test]
    fn test_manhattan_distance() {
        assert_eq!(manhattan_distance((0, 0), (3, 4)), 7);
        assert_eq!(manhattan_distance((1, 1), (1, 1)), 0);
    }
}
