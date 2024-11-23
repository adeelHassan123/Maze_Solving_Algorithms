from pyamaze import maze, agent, COLOR, textLabel

def DLS(m, start, limit):
    """Depth-Limited Search (DLS)"""
    explored = [start]
    frontier = [(start, 0)]  # Track cell with its depth
    dfsPath = {}
    dSearch = []

    while frontier:
        currCell, depth = frontier.pop()
        dSearch.append(currCell)

        if currCell == m._goal:
            break

        if depth < limit:  # Expand only if we're within the depth limit
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
                    explored.append(child)
                    frontier.append((child, depth + 1))  # Increment depth
                    dfsPath[child] = currCell
    return dfsPath, dSearch


def IDS(m):
    """Iterative Deepening Search"""
    start = (m.rows, m.cols)
    limit = 0
    idsPath = None
    dSearch = []

    while True:
        dfsPath, dSearchIter = DLS(m, start, limit)  # Perform depth-limited search
        if m._goal in dfsPath:  # Goal found
            idsPath = dfsPath
            dSearch = dSearchIter
            break
        limit += 1  # Increase depth limit

    # Reconstruct forward path from DFS result
    fwdPath = {}
    cell = m._goal
    while cell != start:
        fwdPath[idsPath[cell]] = cell
        cell = idsPath[cell]
    return dSearch, dfsPath, fwdPath


if __name__ == '__main__':
    # Create a maze of size 10x10
    m = maze(10, 10)
    
    # Create the maze with the goal set to a position in the middle
    m.CreateMaze(5, 5)  # Setting a goal cell in the center (5, 5)

    # Run IDS
    dSearch, dfsPath, fwdPath = IDS(m)

    # Agents for Visualization
    a = agent(m, footprints=True, color=COLOR.blue, filled=True)  # Explored Path
    b = agent(m, 5, 5, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))  # Backtracking Path
    c = agent(m, footprints=True, color=COLOR.red)  # Shortest Path

    # Visualize paths
    m.tracePath({a: dSearch}, showMarked=True, delay=30)  # Show search order
    m.tracePath({b: dfsPath}, delay=30)  # Show explored path
    m.tracePath({c: fwdPath}, delay=30)  # Show the shortest path

    # Run the maze visualization
    m.run()
