from aStarDemo import aStar
from IDSDemo import IDS
from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit

# Create a smaller maze for testing
m = maze(20, 20)
m.CreateMaze(loopPercent=50)  # Reduced complexity of the maze

# Run IDS and GBFS algorithms
isearchPath, idsPath, fwdIDSPath = IDS(m)
searchPath,aPath,fwdPath=aStar(m)

# Output lengths of paths and search orders
textLabel(m, 'DFS Path Length', len(fwdIDSPath) + 1)
l=textLabel(m,'A-Star Path Length',len(fwdPath)+1)
textLabel(m, 'DFS Search Length', len(isearchPath) + 1)
l=textLabel(m,'A-Star Search Length',len(searchPath)+1)

# Create agents for visualization
a = agent(m, footprints=True, color=COLOR.cyan, filled=True)  # For GBFS Path
b = agent(m, footprints=True, color=COLOR.yellow, filled=True)  # For IDS Path

# Visualize the paths
m.tracePath({a: fwdPath}, delay=50)  # Reduced delay
m.tracePath({b: fwdIDSPath}, delay=50)  # Reduced delay

# Time the execution of IDS and GBFS
t1 = timeit(stmt='IDS(m)', number=1, globals=globals())  # Run once instead of 1000
t2 = timeit(stmt='aStar(m)', number=1, globals=globals())  # Run once instead of 1000

# Display the timing results on the maze
textLabel(m, 'DFS Time', t1)
textLabel(m, 'aStar Time', t2)

# Run the maze visualization
m.run()


