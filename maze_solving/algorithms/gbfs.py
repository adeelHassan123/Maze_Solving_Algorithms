"""
Greedy Best-First Search (GBFS) Algorithm implementation for maze solving.
"""

from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue

def manhattan_distance(cell1, cell2):
    """Calculate Manhattan distance between two cells."""
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def greedy_best_first_search(maze_obj):
    """
    Greedy Best-First Search algorithm implementation.
    
    Args:
        maze_obj: pyamaze.maze object representing the maze
        
    Returns:
        dict: Path from start to goal
    """
    start = (maze_obj.rows, maze_obj.cols)
    goal = (1, 1)

    frontier = PriorityQueue()
    frontier.put((manhattan_distance(start, goal), start))
    explored = set()
    came_from = {}

    while not frontier.empty():
        current = frontier.get()[1]
        explored.add(current)

        if current == goal:
            break

        for direction in 'ESNW':
            if maze_obj.maze_map[current][direction]:
                if direction == 'E':
                    neighbor = (current[0], current[1]+1)
                elif direction == 'W':
                    neighbor = (current[0], current[1]-1)
                elif direction == 'N':
                    neighbor = (current[0]-1, current[1])
                elif direction == 'S':
                    neighbor = (current[0]+1, current[1])

                if neighbor in explored:
                    continue

                frontier.put((manhattan_distance(neighbor, goal), neighbor))
                explored.add(neighbor)
                came_from[neighbor] = current

    # Reconstruct path
    path = {}
    current = goal
    while current != start:
        path[came_from[current]] = current
        current = came_from[current]

    return path
