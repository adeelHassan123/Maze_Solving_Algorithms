"""
Breadth-First Search implementation for maze solving.
"""

from collections import deque

def breadth_first_search(maze_obj):
    """
    Breadth-First Search algorithm implementation.
    
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
    
    # Initialize BFS queue and path tracking
    queue = deque([start])
    path = {}
    
    while queue:
        current = queue.popleft()
        maze_obj.expanded_nodes.add(current)  # Mark as expanded when we process it
        
        if current == goal:
            break
            
        # Check each possible direction
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
                    queue.append(neighbor)
                    path[neighbor] = current
    
    # Reconstruct solution path
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[path[cell]] = cell
        cell = path[cell]
        
    return fwdPath
