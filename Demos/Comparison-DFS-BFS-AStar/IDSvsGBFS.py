# from GBFSDemo import GBFS
# from IDSDemo import IDS
# from pyamaze import maze,agent,COLOR,textLabel
# from timeit import timeit

# m=maze(20,30)
# m.CreateMaze(loopPercent=100)
# m.CreateMaze(1,30,loopPercent=100)
# # m.CreateMaze()
# m.CreateMaze(1,30)
# isearchPath,idsPath,fwdIDSPath=IDS(m)
# bSearch,bfsPath,fwdBFSPath=GBFS(m)

# textLabel(m,'DFS Path Length',len(fwdIDSPath)+1)
# textLabel(m,'BFS Path Length',len(fwdBFSPath)+1)
# textLabel(m,'DFS Search Length',len(isearchPath)+1)
# textLabel(m,'BFS Search Length',len(bSearch)+1)

# a=agent(m,footprints=True,color=COLOR.cyan,filled=True)
# b=agent(m,footprints=True,color=COLOR.yellow)
# m.tracePath({a:fwdBFSPath},delay=100)
# m.tracePath({b:fwdIDSPath},delay=100)

# t1=timeit(stmt='IDS(m)',number=1000,globals=globals())
# t2=timeit(stmt='BFS(m)',number=1000,globals=globals())

# textLabel(m,'DFS Time',t1)
# textLabel(m,'BFS Time',t2)


# m.run()

from GBFSDemo import GBFS
from IDSDemo import IDS
from pyamaze import maze, agent, COLOR, textLabel
from timeit import timeit

# Create a smaller maze for testing
m = maze(20, 20)
m.CreateMaze(loopPercent=50)  # Reduced complexity of the maze

# Run IDS and GBFS algorithms
isearchPath, idsPath, fwdIDSPath = IDS(m)
bSearch, gbfsPath, fwdGBFSPath = GBFS(m)

# Output lengths of paths and search orders
textLabel(m, 'DFS Path Length', len(fwdIDSPath) + 1)
textLabel(m, 'GBFS Path Length', len(fwdGBFSPath) + 1)
textLabel(m, 'DFS Search Length', len(isearchPath) + 1)
textLabel(m, 'GBFS Search Length', len(bSearch) + 1)

# Create agents for visualization
a = agent(m, footprints=True, color=COLOR.cyan, filled=True)  # For GBFS Path
b = agent(m, footprints=True, color=COLOR.yellow, filled=True)  # For IDS Path

# Visualize the paths
m.tracePath({a: fwdGBFSPath}, delay=50)  # Reduced delay
m.tracePath({b: fwdIDSPath}, delay=50)  # Reduced delay

# Time the execution of IDS and GBFS
t1 = timeit(stmt='IDS(m)', number=1, globals=globals())  # Run once instead of 1000
t2 = timeit(stmt='GBFS(m)', number=1, globals=globals())  # Run once instead of 1000

# Display the timing results on the maze
textLabel(m, 'DFS Time', t1)
textLabel(m, 'GBFS Time', t2)

# Run the maze visualization
m.run()
