from pyamaze import maze, agent, COLOR
from pyamaze.pyamaze import textLabel


def DLS(m, start, limit):
    """Depth-Limited Search (DLS)"""
    explored = [start]
    frontier = [(start, 0)]  # Keep track of depth with each cell
    dfsPath = {}

    while frontier:
        currCell, depth = frontier.pop()
        if currCell == (1, 1):  # Goal cell
            break
        if depth < limit:  # Expand only within the depth limit
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
                    explored.append(childCell)
                    frontier.append((childCell, depth + 1))  # Increment depth
                    dfsPath[childCell] = currCell
    return dfsPath


def IDS(m):
    """Iterative Deepening Search"""
    start = (m.rows, m.cols)
    limit = 0
    idsPath = None

    while True:
        dfsPath = DLS(m, start, limit)  # Perform depth-limited search
        if (1, 1) in dfsPath:  # Check if goal is reached
            idsPath = dfsPath
            break
        limit += 1  # Increment depth limit

    # Reconstruct forward path from DFS result
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[idsPath[cell]] = cell
        cell = idsPath[cell]
    return fwdPath


if __name__ == '__main__':
    m = maze(15, 10)
    m.CreateMaze(loopPercent=100)

    path = IDS(m)
    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path}, delay=30)

    l = textLabel(m, 'Length of Shortest Path', len(path) + 1)

    m.run()
