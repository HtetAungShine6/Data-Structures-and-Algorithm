from topological_sort import *

V, E = map(int, input().split())

edgeList = []
for i in range(E):
    x = list(map(int, input().split()))
    edgeList.append(x)

print("edgelist: ", edgeList)

vertexList = []
for i in range(len(edgeList)):
    for j in range(2):
        vertexList.append(edgeList[i][j])

vertexList = list(set(vertexList))
vertexList.sort()

print("vertexList: ", vertexList)#...

vertices = len(vertexList)
print("Vertices: ", vertices)#...

adjList = []
for i in range(len(vertexList)):
    temp = [vertexList[i]]
    for edge in edgeList:
        if edge[0] == vertexList[i]:
            temp.append(edge[1])
    
    adjList.append(temp)
print("adjList: ", adjList)

result = topological_sort(len(vertexList), adjList)

print(result)