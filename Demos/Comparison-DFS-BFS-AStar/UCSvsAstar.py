from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit
import heapq
import random

def h(cell1, cell2):
    """Manhattan distance heuristic"""
    return abs(cell1[0] - cell2[0]) + abs(cell1[1] - cell2[1])

def aStar(m):
    """A* algorithm implementation"""
    start = (m.rows, m.cols)
    g_score = {start: 0}
    f_score = {start: h(start, m._goal)}
    
    openSet = [(f_score[start], start)]
    heapq.heapify(openSet)
    aPath = {}
    searchPath = []
    
    while openSet:
        current = heapq.heappop(openSet)[1]
        searchPath.append(current)
        
        if current == m._goal:
            break
            
        for d in 'ESNW':
            if m.maze_map[current][d] == True:
                if d == 'E':
                    childCell = (current[0], current[1] + 1)
                elif d == 'W':
                    childCell = (current[0], current[1] - 1)
                elif d == 'N':
                    childCell = (current[0] - 1, current[1])
                elif d == 'S':
                    childCell = (current[0] + 1, current[1])
                
                temp_g_score = g_score[current] + 1
                
                if childCell not in g_score or temp_g_score < g_score[childCell]:
                    aPath[childCell] = current
                    g_score[childCell] = temp_g_score
                    f_score[childCell] = g_score[childCell] + h(childCell, m._goal)
                    heapq.heappush(openSet, (f_score[childCell], childCell))
    
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[aPath[cell]] = cell
        cell = aPath[cell]
    
    return searchPath, aPath, fwdPath

def UCS(m):
    """Uniform Cost Search implementation with random costs"""
    start = (m.rows, m.cols)
    frontier = [(0, start)]
    heapq.heapify(frontier)
    
    explored = [start]
    ucsPath = {}
    searchOrder = []
    pathCosts = {}
    cellCosts = {start: 0}
    
    while frontier:
        currentCost, currCell = heapq.heappop(frontier)
        searchOrder.append(currCell)
        
        if currCell == m._goal:
            break
            
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                elif d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                elif d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                elif d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                
                if childCell in explored:
                    continue
                
                # Generate random cost between 1 and 10
                moveCost = random.randint(1, 10)
                pathCosts[(currCell, childCell)] = moveCost
                
                explored.append(childCell)
                totalCost = currentCost + moveCost
                cellCosts[childCell] = totalCost
                
                heapq.heappush(frontier, (totalCost, childCell))
                ucsPath[childCell] = currCell
    
    fwdPath = {}
    cell = m._goal
    total_cost = cellCosts[m._goal]
    while cell != start:
        fwdPath[ucsPath[cell]] = cell
        cell = ucsPath[cell]
    
    return searchOrder, ucsPath, fwdPath, total_cost, pathCosts

if __name__ == '__main__':
    # Create maze
    m = maze(20, 20)
    m.CreateMaze(loopPercent=50)

    # Run both algorithms
    ucsSearchOrder, ucsPath, fwdUCSPath, ucs_cost, pathCosts = UCS(m)
    astarSearchPath, astarPath, fwdAStarPath = aStar(m)

    # Create agents for visualization
    a = agent(m, footprints=True, color=COLOR.cyan, filled=True)    # For A*
    b = agent(m, footprints=True, color=COLOR.yellow, filled=True)  # For UCS

    # Add labels for path information
    textLabel(m, 'UCS Path Length', len(fwdUCSPath) + 1)
    textLabel(m, 'A* Path Length', len(fwdAStarPath) + 1)
    textLabel(m, 'UCS Search Length', len(ucsSearchOrder))
    textLabel(m, 'A* Search Length', len(astarSearchPath))
    textLabel(m, 'UCS Total Cost', ucs_cost)

    # Time the algorithms
    t1 = timeit(stmt='UCS(m)', number=1, globals=globals())
    t2 = timeit(stmt='aStar(m)', number=1, globals=globals())

    # Add timing labels
    textLabel(m, 'UCS Time', round(t1, 4))
    textLabel(m, 'A* Time', round(t2, 4))

    # Visualize the paths
    m.tracePath({a: fwdAStarPath}, delay=50)
    m.tracePath({b: fwdUCSPath}, delay=50)

    # Print detailed cost information for UCS path
    print("\nUCS Path Cost Breakdown:")
    current_cell = (m.rows, m.cols)
    total_cost = 0
    path_cells = list(fwdUCSPath.items())
    for (cell1, cell2) in path_cells:
        cost = pathCosts.get((cell1, cell2), pathCosts.get((cell2, cell1)))
        total_cost += cost
        print(f"From {cell1} to {cell2}: Cost = {cost}")
    print(f"Total Path Cost: {total_cost}")

    # Print comparison statistics
    print("\nComparison Statistics:")
    print(f"UCS Path Length: {len(fwdUCSPath) + 1}")
    print(f"A* Path Length: {len(fwdAStarPath) + 1}")
    print(f"UCS Search Length: {len(ucsSearchOrder)}")
    print(f"A* Search Length: {len(astarSearchPath)}")
    print(f"UCS Execution Time: {round(t1, 4)} seconds")
    print(f"A* Execution Time: {round(t2, 4)} seconds")

    # Run the visualization
    m.run()