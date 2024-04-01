n = int(input())
adj_list = []

for _ in range(n):
    adj_list.append(list(map(int,input().split())))

print(adj_list, "\n")

adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

print(adj_matrix, "\n")

for adj in adj_list:
    for i in range(adj[1]):
        adj_matrix[adj[0]-1][adj[i+2]-1] = 1

for row in adj_matrix:
    print(*row)