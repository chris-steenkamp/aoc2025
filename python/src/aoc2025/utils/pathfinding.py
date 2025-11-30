"""Pathfinding utilities.

Common graph traversal and pathfinding algorithms.
"""

from collections import deque
from heapq import heappop, heappush
from typing import Callable, Hashable, Iterable, TypeVar

T = TypeVar("T", bound=Hashable)


def bfs(
    start: T,
    neighbors: Callable[[T], Iterable[T]],
    goal: Callable[[T], bool],
) -> list[T] | None:
    """Breadth-first search for unweighted shortest path.
    
    Args:
        start: Starting node
        neighbors: Function that returns neighbors of a node
        goal: Function that returns True if node is the goal
        
    Returns:
        List of nodes from start to goal (inclusive), or None if no path exists.
    """
    if goal(start):
        return [start]
    
    queue: deque[tuple[T, list[T]]] = deque([(start, [start])])
    visited: set[T] = {start}
    
    while queue:
        current, path = queue.popleft()
        
        for next_node in neighbors(current):
            if next_node in visited:
                continue
            
            new_path = path + [next_node]
            
            if goal(next_node):
                return new_path
            
            visited.add(next_node)
            queue.append((next_node, new_path))
    
    return None


def dijkstra(
    start: T,
    neighbors: Callable[[T], Iterable[tuple[T, int]]],
    goal: Callable[[T], bool],
) -> tuple[list[T], int] | None:
    """Dijkstra's algorithm for weighted shortest path.
    
    Args:
        start: Starting node
        neighbors: Function that returns (neighbor, cost) tuples
        goal: Function that returns True if node is the goal
        
    Returns:
        Tuple of (path, total_cost), or None if no path exists.
    """
    if goal(start):
        return ([start], 0)
    
    # Priority queue: (cost, node, path)
    heap: list[tuple[int, T, list[T]]] = [(0, start, [start])]
    visited: set[T] = set()
    
    while heap:
        cost, current, path = heappop(heap)
        
        if current in visited:
            continue
        visited.add(current)
        
        if goal(current):
            return (path, cost)
        
        for next_node, edge_cost in neighbors(current):
            if next_node not in visited:
                new_cost = cost + edge_cost
                new_path = path + [next_node]
                heappush(heap, (new_cost, next_node, new_path))
    
    return None


def astar(
    start: T,
    neighbors: Callable[[T], Iterable[tuple[T, int]]],
    heuristic: Callable[[T], int],
    goal: Callable[[T], bool],
) -> tuple[list[T], int] | None:
    """A* search algorithm for weighted shortest path with heuristic.
    
    Args:
        start: Starting node
        neighbors: Function that returns (neighbor, cost) tuples
        heuristic: Function estimating cost from node to goal (must not overestimate)
        goal: Function that returns True if node is the goal
        
    Returns:
        Tuple of (path, total_cost), or None if no path exists.
    """
    if goal(start):
        return ([start], 0)
    
    # Priority queue: (estimated_total, actual_cost, node, path)
    heap: list[tuple[int, int, T, list[T]]] = [(heuristic(start), 0, start, [start])]
    visited: set[T] = set()
    
    while heap:
        _, cost, current, path = heappop(heap)
        
        if current in visited:
            continue
        visited.add(current)
        
        if goal(current):
            return (path, cost)
        
        for next_node, edge_cost in neighbors(current):
            if next_node not in visited:
                new_cost = cost + edge_cost
                new_path = path + [next_node]
                estimated = new_cost + heuristic(next_node)
                heappush(heap, (estimated, new_cost, next_node, new_path))
    
    return None


def flood_fill(
    start: T,
    neighbors: Callable[[T], Iterable[T]],
) -> set[T]:
    """Find all nodes reachable from start using BFS.
    
    Args:
        start: Starting node
        neighbors: Function that returns neighbors of a node
        
    Returns:
        Set of all reachable nodes including start.
    """
    visited: set[T] = {start}
    queue: deque[T] = deque([start])
    
    while queue:
        current = queue.popleft()
        
        for next_node in neighbors(current):
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    
    return visited
