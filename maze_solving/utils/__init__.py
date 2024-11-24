"""
Utility functions for maze solving algorithms.
"""

def get_neighbor(current, direction):
    """
    Get neighboring cell coordinates based on direction.
    
    Args:
        current (tuple): Current cell coordinates (row, col)
        direction (str): Direction to move ('E', 'W', 'N', 'S')
        
    Returns:
        tuple: Coordinates of the neighbor cell
    """
    if direction == 'E':
        return (current[0], current[1]+1)
    elif direction == 'W':
        return (current[0], current[1]-1)
    elif direction == 'N':
        return (current[0]-1, current[1])
    elif direction == 'S':
        return (current[0]+1, current[1])
    return None

def reconstruct_path(came_from, start, goal):
    """
    Reconstruct path from start to goal using came_from dictionary.
    
    Args:
        came_from (dict): Dictionary mapping each cell to its predecessor
        start (tuple): Start cell coordinates
        goal (tuple): Goal cell coordinates
        
    Returns:
        dict: Path from start to goal
    """
    path = {}
    current = goal
    while current != start:
        path[came_from[current]] = current
        current = came_from[current]
    return path
