from pyamaze import maze, agent, COLOR, textLabel
import heapq
import random

def UCS(m):
    """Uniform Cost Search with visualization paths and random costs"""
    start = (m.rows, m.cols)
    frontier = [(0, start)]  # (total_cost, cell)
    heapq.heapify(frontier)
    
    explored = [start]
    ucsPath = {}  # Stores the complete exploration path
    searchOrder = []  # Stores the order of cells visited
    pathCosts = {}  # Stores the cost between adjacent cells
    cellCosts = {start: 0}  # Stores the total cost to reach each cell
    
    while frontier:
        currentTotalCost, currCell = heapq.heappop(frontier)
        searchOrder.append(currCell)
        
        if currCell == m._goal:
            break
            
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    child = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    child = (currCell[0], currCell[1] - 1)
                if d == 'N':
                    child = (currCell[0] - 1, currCell[1])
                if d == 'S':
                    child = (currCell[0] + 1, currCell[1])
                
                if child in explored:
                    continue
                
                # Generate random cost for this move (between 1 and 10)
                moveCost = random.randint(1, 10)
                pathCosts[(currCell, child)] = moveCost
                
                explored.append(child)
                totalCost = currentTotalCost + moveCost
                cellCosts[child] = totalCost
                
                heapq.heappush(frontier, (totalCost, child))
                ucsPath[child] = currCell

    # Reconstruct forward path
    fwdPath = {}
    cell = m._goal
    pathCostBreakdown = []  # Store cost breakdown for the shortest path
    while cell != start:
        prev_cell = ucsPath[cell]
        fwdPath[prev_cell] = cell
        # Store the cost for this segment
        segment_cost = pathCosts.get((prev_cell, cell), pathCosts.get((cell, prev_cell)))
        pathCostBreakdown.append((prev_cell, cell, segment_cost))
        cell = prev_cell
        
    return searchOrder, ucsPath, fwdPath, pathCosts, cellCosts, pathCostBreakdown


if __name__ == '__main__':
    # Create a maze of size 10x10
    m = maze(10, 10)
    
    # Create the maze with the goal set to a position in the middle
    m.CreateMaze(5, 5)  # Setting a goal cell in the center (5, 5)

    # Run UCS
    searchOrder, exploredPath, shortestPath, pathCosts, cellCosts, pathCostBreakdown = UCS(m)

    # Calculate total cost of the shortest path
    total_cost = sum(cost for _, _, cost in pathCostBreakdown)

    # Agents for Visualization
    a = agent(m, footprints=True, color=COLOR.blue, filled=True)    # Search Order
    b = agent(m, 5, 5, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))  # Explored Path
    c = agent(m, footprints=True, color=COLOR.red)    # Shortest Path

    # Visualize the different paths
    m.tracePath({a: searchOrder}, showMarked=True, delay=30)  # Show search order
    m.tracePath({b: exploredPath}, delay=30)  # Show explored path
    m.tracePath({c: shortestPath}, delay=30)  # Show the shortest path

    # Add labels for path information
    l1 = textLabel(m, 'Path Length', len(shortestPath) + 1)
    l2 = textLabel(m, 'Total Cost', total_cost)

    # Print detailed path cost information
    print("\nShortest Path Cost Breakdown:")
    for start_cell, end_cell, cost in reversed(pathCostBreakdown):
        print(f"From {start_cell} to {end_cell}: Cost = {cost}")
    print(f"\nTotal Path Cost: {total_cost}")

    # Print costs for all explored cells
    print("\nTotal Cost to Reach Each Cell:")
    for cell, cost in sorted(cellCosts.items()):
        print(f"Cell {cell}: Total Cost = {cost}")

    # Run the maze visualization
    m.run()