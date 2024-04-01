def create_adjacency_matrix(vertices, edges):
    no_of_vertices = len(vertices)
    adjacency_matrix = [[0 for _ in range(no_of_vertices)] for _ in range(no_of_vertices)]

    for edge in edges:
        i, j = edge
        if i >= no_of_vertices or j >= no_of_vertices or i < 0 or j < 0:
            print(f"Not a proper input in edge {i},{j}")
        else:
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1  

    return adjacency_matrix

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
print("Vertices: ", vertices)

adj_matrix = create_adjacency_matrix(vertices, edgeList)

for row in adj_matrix:
    print(row)
