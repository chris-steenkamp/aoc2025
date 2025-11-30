//! Grid utilities for 2D puzzle grids
//!
//! Provides a generic Grid type for working with 2D arrays.

use std::fmt::Display;

/// A 2D grid of values
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Grid<T> {
    data: Vec<T>,
    pub width: usize,
    pub height: usize,
}

impl<T: Clone> Grid<T> {
    /// Create a new grid with the given dimensions, filled with a default value
    pub fn new(width: usize, height: usize, default: T) -> Self {
        Self {
            data: vec![default; width * height],
            width,
            height,
        }
    }

    /// Create a grid from a 2D vector
    pub fn from_vec(data: Vec<Vec<T>>) -> Option<Self> {
        if data.is_empty() {
            return None;
        }
        let height = data.len();
        let width = data[0].len();

        // Ensure all rows have the same width
        if !data.iter().all(|row| row.len() == width) {
            return None;
        }

        let flat: Vec<T> = data.into_iter().flatten().collect();
        Some(Self {
            data: flat,
            width,
            height,
        })
    }

    /// Get the value at (x, y) coordinates
    pub fn get(&self, x: usize, y: usize) -> Option<&T> {
        if x < self.width && y < self.height {
            Some(&self.data[y * self.width + x])
        } else {
            None
        }
    }

    /// Get a mutable reference to the value at (x, y) coordinates
    pub fn get_mut(&mut self, x: usize, y: usize) -> Option<&mut T> {
        if x < self.width && y < self.height {
            Some(&mut self.data[y * self.width + x])
        } else {
            None
        }
    }

    /// Set the value at (x, y) coordinates
    pub fn set(&mut self, x: usize, y: usize, value: T) -> bool {
        if x < self.width && y < self.height {
            self.data[y * self.width + x] = value;
            true
        } else {
            false
        }
    }

    /// Get the 4 cardinal neighbors (N, S, E, W) of a position
    pub fn neighbors(&self, x: usize, y: usize) -> Vec<(usize, usize)> {
        let mut result = Vec::with_capacity(4);
        
        if y > 0 {
            result.push((x, y - 1)); // North
        }
        if y + 1 < self.height {
            result.push((x, y + 1)); // South
        }
        if x > 0 {
            result.push((x - 1, y)); // West
        }
        if x + 1 < self.width {
            result.push((x + 1, y)); // East
        }
        
        result
    }

    /// Get all 8 neighbors including diagonals
    pub fn neighbors_diagonal(&self, x: usize, y: usize) -> Vec<(usize, usize)> {
        let mut result = Vec::with_capacity(8);
        
        for dy in -1i32..=1 {
            for dx in -1i32..=1 {
                if dx == 0 && dy == 0 {
                    continue;
                }
                let nx = x as i32 + dx;
                let ny = y as i32 + dy;
                if nx >= 0 && ny >= 0 && (nx as usize) < self.width && (ny as usize) < self.height {
                    result.push((nx as usize, ny as usize));
                }
            }
        }
        
        result
    }

    /// Iterate over all positions and values
    pub fn iter(&self) -> impl Iterator<Item = ((usize, usize), &T)> {
        self.data.iter().enumerate().map(move |(i, v)| {
            let x = i % self.width;
            let y = i / self.width;
            ((x, y), v)
        })
    }

    /// Find the first position matching a predicate
    pub fn find<F>(&self, predicate: F) -> Option<(usize, usize)>
    where
        F: Fn(&T) -> bool,
    {
        self.iter()
            .find(|(_, v)| predicate(v))
            .map(|(pos, _)| pos)
    }
}

impl Grid<char> {
    /// Parse a grid from a multi-line string
    pub fn from_str(input: &str) -> Option<Self> {
        let data: Vec<Vec<char>> = input
            .lines()
            .filter(|line| !line.is_empty())
            .map(|line| line.chars().collect())
            .collect();
        Self::from_vec(data)
    }
}

impl<T: Display> Display for Grid<T> {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        for y in 0..self.height {
            for x in 0..self.width {
                write!(f, "{}", self.data[y * self.width + x])?;
            }
            writeln!(f)?;
        }
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_grid_creation() {
        let grid: Grid<i32> = Grid::new(3, 2, 0);
        assert_eq!(grid.width, 3);
        assert_eq!(grid.height, 2);
        assert_eq!(grid.get(0, 0), Some(&0));
    }

    #[test]
    fn test_grid_neighbors() {
        let grid: Grid<i32> = Grid::new(3, 3, 0);
        let neighbors = grid.neighbors(1, 1);
        assert_eq!(neighbors.len(), 4);
    }
}
