"""
Iterative Deepening Search (IDS) Algorithm implementation for maze solving.
"""

def depth_limited_search(maze_obj, start, goal, depth_limit, explored, came_from):
    """Helper function for IDS that performs depth-limited search."""
    if depth_limit == 0 and start == goal:
        return True
    
    if depth_limit > 0:
        for direction in 'ESNW':
            if maze_obj.maze_map[start][direction]:
                if direction == 'E':
                    neighbor = (start[0], start[1]+1)
                elif direction == 'W':
                    neighbor = (start[0], start[1]-1)
                elif direction == 'N':
                    neighbor = (start[0]-1, start[1])
                elif direction == 'S':
                    neighbor = (start[0]+1, start[1])
                    
                if neighbor not in explored:
                    explored.add(neighbor)
                    came_from[neighbor] = start
                    
                    if depth_limited_search(maze_obj, neighbor, goal, depth_limit-1, explored, came_from):
                        return True
                        
    return False

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
    max_depth = maze_obj.rows * maze_obj.cols  # Maximum possible path length
    
    for depth in range(max_depth):
        explored = {start}
        came_from = {}
        
        if depth_limited_search(maze_obj, start, goal, depth, explored, came_from):
            # Reconstruct path
            path = {}
            current = goal
            while current != start:
                path[came_from[current]] = current
                current = came_from[current]
            return path
            
    return {}  # No path found
