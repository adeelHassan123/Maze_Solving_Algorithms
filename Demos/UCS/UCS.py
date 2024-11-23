from pyamaze import maze, agent, COLOR
from pyamaze.pyamaze import textLabel
import heapq
import random

def UCS(m, start):
    """Uniform Cost Search implementation for maze solving with random path costs"""
    frontier = [(0, start)]
    heapq.heapify(frontier)
    explored = [start]
    ucsPath = {}
    pathCosts = {}  # Dictionary to store costs between cells
    
    while frontier:
        current_cost, currCell = heapq.heappop(frontier)
        
        if currCell == (1, 1):  # Goal cell
            break
            
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                
                if childCell in explored:
                    continue
                
                # Generate random cost for this move (between 1 and 10)
                move_cost = random.randint(1, 10)
                
                # Store the cost for this path segment
                pathCosts[(currCell, childCell)] = move_cost
                
                explored.append(childCell)
                heapq.heappush(frontier, (current_cost + move_cost, childCell))
                ucsPath[childCell] = currCell
    
    # Reconstruct forward path
    fwdPath = {}
    cell = (1, 1)
    total_cost = 0
    while cell != start:
        prev_cell = ucsPath[cell]
        fwdPath[prev_cell] = cell
        # Add the cost of this path segment to total
        if (prev_cell, cell) in pathCosts:
            total_cost += pathCosts[(prev_cell, cell)]
        cell = prev_cell
    
    return fwdPath, total_cost, pathCosts


if __name__ == '__main__':
    m = maze(15, 10)
    m.CreateMaze(loopPercent=100)

    start = (m.rows, m.cols)
    path, total_cost, pathCosts = UCS(m, start)
    
    # Create and configure the agent
    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path}, delay=30)

    # Display path length and total cost
    l1 = textLabel(m, 'Length of Path', len(path)+1)
    l2 = textLabel(m, 'Total Cost', total_cost)

    # Optional: Print individual path segment costs
    print("\nPath segment costs:")
    for (cell1, cell2), cost in pathCosts.items():
        if cell1 in path and path[cell1] == cell2:
            print(f"From {cell1} to {cell2}: Cost = {cost}")

    m.run()