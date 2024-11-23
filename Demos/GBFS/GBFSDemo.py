from pyamaze import maze, agent, textLabel, COLOR
from queue import PriorityQueue


def h(cell1, cell2):
    """Heuristic function: Manhattan distance"""
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def GBFS(m, start=None):
    if start is None:
        start = (m.rows, m.cols)

    # Priority queue for GBFS
    frontier = PriorityQueue()
    goal = (1, 1)
    frontier.put((h(start, goal), start))  # (heuristic, cell)

    gbfsPath = {}
    explored = [start]
    gSearch = []  # To visualize the search order

    while not frontier.empty():
        currCell = frontier.get()[1]  # Get the cell with the smallest heuristic
        if currCell == goal:
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

                frontier.put((h(childCell, goal), childCell))  # Add child based on heuristic
                explored.append(childCell)
                gbfsPath[childCell] = currCell
                gSearch.append(childCell)

    # Reconstruct forward path
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[gbfsPath[cell]] = cell
        cell = gbfsPath[cell]

    return gSearch, gbfsPath, fwdPath


if __name__ == '__main__':
    m = maze(20, 20)
    m.CreateMaze(loopPercent=10, theme='dark')

    gSearch, gbfsPath, fwdPath = GBFS(m)

    a = agent(m, footprints=True, color=COLOR.blue, filled=True)  # Explored Path
    b = agent(m, 1, 1, footprints=True, color=COLOR.yellow, filled=True, goal=(m.rows, m.cols))  # A* Backtracking Path
    c = agent(m, footprints=True, color=COLOR.red)  # Shortest Path
    
    # b = agent(m, footprints=True, color=COLOR.yellow, shape='square', filled=False)  # GBFS Backtracking
    # c = agent(m, 1, 1, footprints=True, color=COLOR.red, shape='square', filled=True, goal=(m.rows, m.cols))  # Shortest path

    # Visualize the paths
    m.tracePath({a: gSearch}, delay=30)
    m.tracePath({b: gbfsPath}, delay=30)
    m.tracePath({c: fwdPath}, delay=30)

    m.run()
