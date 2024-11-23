from pyamaze import maze,COLOR,agent
m=maze(45,50)

m.CreateMaze(loopPercent=50)

a=agent(m,footprints=True,filled=True)
b=agent(m,5,5,footprints=True,color='red')
c=agent(m,4,1,footprints=True,color='green',shape='arrow')


path2=[(5,4),(5,3),(4,3),(3,3),(3,4),(4,4)]
path3='WWNNES'


m.tracePath({a:m.path,b:path2,c:path3},delay=20,kill=False)

m.run()
