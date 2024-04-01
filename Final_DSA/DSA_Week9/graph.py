class Graph:
    def __init__(self):
        self.edge_list = []    # List to store edges
        self.vertices = set()  # Set to store vertices

    def add_edge(self, u, v):
        self.edge_list.append((u, v))
        self.vertices.add(u)
        self.vertices.add(v)

    def adjacency_list(self):
        adj_list = {v: [] for v in self.vertices}
        for u, v in self.edge_list:
            adj_list[u].append(v)
            adj_list[v].append(u)  # Uncomment for undirected graph
        return adj_list

    def adjacency_matrix(self):
        n = len(self.vertices)
        adj_matrix = [[0] * n for _ in range(n)]
        vertex_index = {vertex: i for i, vertex in enumerate(sorted(self.vertices))}
        for u, v in self.edge_list:
            adj_matrix[vertex_index[u]][vertex_index[v]] = 1
            adj_matrix[vertex_index[v]][vertex_index[u]] = 1  # Uncomment for undirected graph
        return adj_matrix

    def display(self):
        print("Edge List:")
        print(self.edge_list)
        print("\nVertices List:")
        print(sorted(self.vertices))
        print("\nAdjacency List:")
        print(self.adjacency_list())
        print("\nAdjacency Matrix:")
        for row in self.adjacency_matrix():
            print(row)


# Example usage:
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'A')
graph.add_edge('B', 'D')
graph.add_edge('D', 'A')
graph.add_edge('D', 'E')
graph.add_edge('E', 'B')

graph.display()
