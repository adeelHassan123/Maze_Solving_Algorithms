"""
Iterative Deepening Search (IDS) Algorithm implementation for maze solving.
"""

def depth_limited_search(maze_obj, start, goal, depth_limit, expanded_nodes, explored_cells, visited):
    """Helper function for IDS that performs depth-limited search."""
    if start == goal:
        return True, {}
    
    if depth_limit <= 0:
        return False, {}
    
    # Mark current node as expanded and visited
    expanded_nodes.add(start)
    visited.add(start)
    
    # Check all possible directions
    for direction in 'ESNW':
        if maze_obj.maze_map[start][direction]:
            # Calculate neighbor coordinates
            if direction == 'E':
                neighbor = (start[0], start[1]+1)
            elif direction == 'W':
                neighbor = (start[0], start[1]-1)
            elif direction == 'N':
                neighbor = (start[0]-1, start[1])
            else:  # S
                neighbor = (start[0]+1, start[1])
            
            # Mark cell as explored when we first see it
            explored_cells.add(neighbor)
            
            # Skip if we've already visited this node in current path
            if neighbor in visited:
                continue
                
            # Recursively search from neighbor
            found, child_path = depth_limited_search(
                maze_obj, neighbor, goal, depth_limit-1,
                expanded_nodes, explored_cells, visited
            )
            
            if found:
                child_path[start] = neighbor
                return True, child_path
    
    # Remove from visited when backtracking
    visited.remove(start)
    return False, {}

def iterative_deepening_search(maze_obj):
    """
    Iterative Deepening Search algorithm implementation.
    
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
    
    # Maximum depth is Manhattan distance * 2 for a reasonable upper bound
    max_depth = (maze_obj.rows + maze_obj.cols) * 2
    
    for depth in range(1, max_depth + 1):
        visited = set()  # Track visited nodes for current iteration
        found, path = depth_limited_search(
            maze_obj, start, goal, depth,
            maze_obj.expanded_nodes, maze_obj.explored_cells, visited
        )
        if found:
            return path
            
    return {}
