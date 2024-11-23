from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit
import heapq
import random

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

def DFS(m, start, goal, path, depthlimit):
    """Depth-First Search with depth limit"""
    path.append(start)
    
    if start == goal:
        return True
    
    if depthlimit <= 0:
        path.pop()
        return False
    
    for d in 'ESNW':
        if m.maze_map[start][d] == True:
            if d == 'E':
                newCell = (start[0], start[1] + 1)
            elif d == 'W':
                newCell = (start[0], start[1] - 1)
            elif d == 'N':
                newCell = (start[0] - 1, start[1])
            elif d == 'S':
                newCell = (start[0] + 1, start[1])
            
            if newCell not in path:
                if DFS(m, newCell, goal, path, depthlimit - 1):
                    return True
    
    path.pop()
    return False

def IDS(m):
    """Iterative Deepening Search implementation"""
    start = (m.rows, m.cols)
    goal = m._goal
    searchPath = []
    
    for depth in range(m.rows * m.cols):
        path = []
        if DFS(m, start, goal, path, depth):
            idsPath = {}
            fwdPath = {}
            for i in range(len(path)-1):
                idsPath[path[i+1]] = path[i]
            for i in range(len(path)-1):
                fwdPath[path[i]] = path[i+1]
            searchPath.extend(path)
            return searchPath, idsPath, fwdPath
        searchPath.extend(path)
    
    return None

if __name__ == '__main__':
    # Create maze
    m = maze(20, 20)
    m.CreateMaze(loopPercent=50)

    # Run both algorithms
    ucsSearchOrder, ucsPath, fwdUCSPath, ucs_cost, pathCosts = UCS(m)
    idsSearchPath, idsPath, fwdIDSPath = IDS(m)

    # Create agents for visualization
    a = agent(m, footprints=True, color=COLOR.cyan, filled=True)    # For IDS
    b = agent(m, footprints=True, color=COLOR.yellow, filled=True)  # For UCS

    # Add labels for path information
    textLabel(m, 'UCS Path Length', len(fwdUCSPath) + 1)
    textLabel(m, 'IDS Path Length', len(fwdIDSPath) + 1)
    textLabel(m, 'UCS Search Length', len(ucsSearchOrder))
    textLabel(m, 'IDS Search Length', len(idsSearchPath))
    textLabel(m, 'UCS Total Cost', ucs_cost)

    # Time the algorithms
    t1 = timeit(stmt='UCS(m)', number=1, globals=globals())
    t2 = timeit(stmt='IDS(m)', number=1, globals=globals())

    # Add timing labels
    textLabel(m, 'UCS Time', round(t1, 4))
    textLabel(m, 'IDS Time', round(t2, 4))

    # Visualize the paths
    m.tracePath({a: fwdIDSPath}, delay=50)
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
    print(f"IDS Path Length: {len(fwdIDSPath) + 1}")
    print(f"UCS Search Length: {len(ucsSearchOrder)}")
    print(f"IDS Search Length: {len(idsSearchPath)}")
    print(f"UCS Execution Time: {round(t1, 4)} seconds")
    print(f"IDS Execution Time: {round(t2, 4)} seconds")

    # Run the visualization
    m.run()