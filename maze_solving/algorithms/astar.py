"""
A* Search Algorithm implementation for maze solving.
"""

from pyamaze import maze, agent, textLabel
from queue import PriorityQueue

def manhattan_distance(cell1, cell2):
    """Calculate Manhattan distance between two cells."""
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1-x2) + abs(y1-y2)

def astar_search(maze_obj):
    """
    A* Search algorithm implementation.
    
    Args:
        maze_obj: pyamaze.maze object representing the maze
        
    Returns:
        dict: Path from start to goal
    """
    start = (maze_obj.rows, maze_obj.cols)
    goal = (1, 1)
    
    g_score = {cell: float('inf') for cell in maze_obj.grid}
    g_score[start] = 0
    f_score = {cell: float('inf') for cell in maze_obj.grid}
    f_score[start] = manhattan_distance(start, goal)

    open_set = PriorityQueue()
    open_set.put((manhattan_distance(start, goal), manhattan_distance(start, goal), start))
    came_from = {}
    
    # Track explored and expanded nodes separately
    maze_obj.explored_cells = set()  # All cells we've seen
    maze_obj.expanded_nodes = set()  # Cells we've actually expanded

    while not open_set.empty():
        current = open_set.get()[2]
        maze_obj.expanded_nodes.add(current)  # Count as expanded when we process it
        
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

                maze_obj.explored_cells.add(neighbor)  # Count as explored when we see it
                
                tentative_g = g_score[current] + 1
                tentative_f = tentative_g + manhattan_distance(neighbor, goal)

                if tentative_f < f_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_f
                    open_set.put((tentative_f, manhattan_distance(neighbor, goal), neighbor))
                    came_from[neighbor] = current

    # Reconstruct path
    path = {}
    current = goal
    while current != start:
        path[came_from[current]] = current
        current = came_from[current]
        
    return path
