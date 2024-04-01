n = int(input())
adj_list = [list(map(int, input().split())) for _ in range(n)]

color = ["WHITE"]*n
d = [-1]*n
p = [None]*n

s = adj_list[0][0] - 1
color[s] = "GREY"
d[s] = 0
p[s] = None

Q = [s]
while Q:
    u = Q[0]
    del Q[0]

    for i in range(adj_list[u][1]):
        v = adj_list[u][i+2] - 1
        if color[v] == "WHITE":
            color[v] = "GREY"
            d[v] = d[u] + 1
            p[v] = u
            Q.append((v))

    color[u] = "BLACK"

for v in range(n):
    print(*(v+1,d[v]))