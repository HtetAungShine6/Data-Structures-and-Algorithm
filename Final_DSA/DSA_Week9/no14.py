def create_adjacency_matrix(vertices, edges, edge_list):
    adjacency_matrix = [[0] * vertices for _ in range(vertices)]

    for edge in edge_list:
        vertex1, vertex2, weight = edge
        adjacency_matrix[vertex1][vertex2] = weight
        adjacency_matrix[vertex2][vertex1] = weight  # Assuming undirected graph

    return adjacency_matrix

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    edge_list = []
    print("Enter the edges in the format 'vertex1 vertex2 weight':")
    for _ in range(edges):
        edge = list(map(int, input().split()))
        edge_list.append(edge)

    adjacency_matrix = create_adjacency_matrix(vertices, edges, edge_list)

    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)

if __name__ == "__main__":
    main()

# Enter the number of vertices: 4
# Enter the number of edges: 5
# Enter the edges in the format 'vertex1 vertex2 weight':
# 0 1 2
# 0 2 3
# 1 2 1
# 1 3 4
# 2 3 5