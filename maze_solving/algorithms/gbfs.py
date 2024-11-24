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

    # Initialize tracking sets
    maze_obj.expanded_nodes = set()  # Nodes we've processed
    maze_obj.explored_cells = set()  # Cells we've seen
    maze_obj.explored_cells.add(start)  # Start is immediately seen

    frontier = PriorityQueue()
    frontier.put((manhattan_distance(start, goal), start))
    came_from = {}

    while not frontier.empty():
        current = frontier.get()[1]
        maze_obj.expanded_nodes.add(current)  # Mark as expanded when we process it

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

                if neighbor not in maze_obj.explored_cells:
                    maze_obj.explored_cells.add(neighbor)  # Mark as explored when we first see it
                    frontier.put((manhattan_distance(neighbor, goal), neighbor))
                    came_from[neighbor] = current

    # Reconstruct path
    path = {}
    current = goal
    while current != start:
        path[came_from[current]] = current
        current = came_from[current]

    return path
