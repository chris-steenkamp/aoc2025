//! Pathfinding utilities
//!
//! This module re-exports useful items from the `pathfinding` crate
//! and provides some convenience wrappers.
//!
//! The `pathfinding` crate provides:
//! - `bfs` - Breadth-first search (unweighted shortest path)
//! - `dijkstra` - Weighted shortest path
//! - `astar` - Heuristic-guided shortest path
//! - `dfs` - Depth-first search
//!
//! See https://docs.rs/pathfinding for full documentation.

// Re-export commonly used items from the pathfinding crate
pub use pathfinding::prelude::{astar, bfs, dijkstra};

// Example usage patterns (uncomment and modify as needed):
//
// BFS (unweighted shortest path):
// ```
// let result = bfs(
//     &start,
//     |&pos| get_neighbors(pos),
//     |&pos| pos == goal,
// );
// ```
//
// Dijkstra (weighted shortest path):
// ```
// let result = dijkstra(
//     &start,
//     |&pos| get_neighbors_with_costs(pos),
//     |&pos| pos == goal,
// );
// ```
//
// A* (heuristic shortest path):
// ```
// let result = astar(
//     &start,
//     |&pos| get_neighbors_with_costs(pos),
//     |&pos| heuristic(pos, goal),
//     |&pos| pos == goal,
// );
// ```

/// Find all positions reachable from a start position using BFS
/// Returns a set of all visited positions
pub fn flood_fill<N, FN, IN>(start: N, mut successors: FN) -> std::collections::HashSet<N>
where
    N: Eq + std::hash::Hash + Clone,
    FN: FnMut(&N) -> IN,
    IN: IntoIterator<Item = N>,
{
    use std::collections::{HashSet, VecDeque};
    
    let mut visited = HashSet::new();
    let mut queue = VecDeque::new();
    
    visited.insert(start.clone());
    queue.push_back(start);
    
    while let Some(current) = queue.pop_front() {
        for next in successors(&current) {
            if !visited.contains(&next) {
                visited.insert(next.clone());
                queue.push_back(next);
            }
        }
    }
    
    visited
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_bfs_simple() {
        // Simple grid pathfinding test
        let start = (0i32, 0i32);
        let goal = (2i32, 2i32);
        
        let result = bfs(
            &start,
            |&(x, y)| {
                vec![(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
                    .into_iter()
                    .filter(|&(nx, ny)| nx >= 0 && ny >= 0 && nx <= 3 && ny <= 3)
            },
            |&pos| pos == goal,
        );
        
        assert!(result.is_some());
        let path = result.unwrap();
        assert_eq!(path.len(), 5); // Start + 4 moves
    }

    #[test]
    fn test_flood_fill() {
        let visited = flood_fill((0i32, 0i32), |&(x, y)| {
            vec![(x + 1, y), (x, y + 1)]
                .into_iter()
                .filter(|&(nx, ny)| nx <= 2 && ny <= 2)
        });
        
        // Should visit a triangle of positions
        assert!(visited.contains(&(0, 0)));
        assert!(visited.contains(&(1, 0)));
        assert!(visited.contains(&(0, 1)));
    }
}
