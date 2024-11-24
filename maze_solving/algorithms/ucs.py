"""
Uniform Cost Search (UCS) Algorithm implementation for maze solving.
"""

from queue import PriorityQueue

def uniform_cost_search(maze_obj):
    """
    Uniform Cost Search algorithm implementation.
    
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

    # Priority queue ordered by cumulative cost
    frontier = PriorityQueue()
    frontier.put((0, start))  # (cost, cell)
    
    # Track paths and costs
    came_from = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        current_cost, current = frontier.get()
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
                
                # Get the cost of moving to this neighbor
                move_cost = maze_obj.maze_map[current].get('cost', 1)  # Default to 1 if no cost specified
                new_cost = cost_so_far[current] + move_cost

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    maze_obj.explored_cells.add(neighbor)  # Mark as explored when we first see it
                    cost_so_far[neighbor] = new_cost
                    frontier.put((new_cost, neighbor))
                    came_from[neighbor] = current

    # Reconstruct path
    path = {}
    current = goal
    while current != start:
        path[came_from[current]] = current
        current = came_from[current]

    return path
