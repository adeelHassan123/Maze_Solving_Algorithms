from pyamaze import maze, agent, COLOR, textLabel
from queue import PriorityQueue


def h(cell1, cell2):
    """Heuristic function: Manhattan distance"""
    x1, y1 = cell1
    x2, y2 = cell2
    return abs(x1 - x2) + abs(y1 - y2)


def GBFS(m):
    start = (m.rows, m.cols)
    goal = (1, 1)

    # Priority queue for Greedy Best-First Search
    frontier = PriorityQueue()
    frontier.put((h(start, goal), start))  # (heuristic, cell)

    explored = []
    gbfsPath = {}

    while not frontier.empty():
        currCell = frontier.get()[1]  # Get the cell with the smallest heuristic
        explored.append(currCell)

        if currCell == goal:
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

                frontier.put((h(childCell, goal), childCell))
                explored.append(childCell)
                gbfsPath[childCell] = currCell

    # Reconstruct forward path
    fwdPath = {}
    cell = goal
    while cell != start:
        fwdPath[gbfsPath[cell]] = cell
        cell = gbfsPath[cell]

    return fwdPath


if __name__ == '__main__':
    m = maze(20, 20)
    m.CreateMaze(loopPercent=40)

    path = GBFS(m)

    a = agent(m, footprints=True, filled=True)
    m.tracePath({a: path}, delay=30)

    l = textLabel(m, 'Length of Shortest Path', len(path) + 1)

    m.run()
