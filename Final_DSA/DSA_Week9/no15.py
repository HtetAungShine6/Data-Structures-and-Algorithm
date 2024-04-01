def create_adjacency_lists(vertices, edges, edge_list):
    adjacency_lists = [[] for _ in range(vertices)]

    for edge in edge_list:
        vertex1, vertex2, weight = edge
        adjacency_lists[vertex1].append((vertex2, weight))
        adjacency_lists[vertex2].append((vertex1, weight))  # Assuming undirected graph

    return adjacency_lists

def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    edge_list = []
    print("Enter the edges in the format 'vertex1 vertex2 weight':")
    for _ in range(edges):
        edge = list(map(int, input().split()))
        edge_list.append(edge)

    adjacency_lists = create_adjacency_lists(vertices, edges, edge_list)

    print("Adjacency Lists:")
    for vertex, adjacency_list in enumerate(adjacency_lists):
        print(f"Vertex {vertex}: {adjacency_list}")

if __name__ == "__main__":
    main()
