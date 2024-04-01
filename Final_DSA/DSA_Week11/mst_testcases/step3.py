# Name - Htet Aung Shine
# ID - 6530145
# Section - 542

V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

print(edgeList)


from disjointsets3 import DisjointSets

s = DisjointSets(V)

# Complete the code below

edgeList.sort(key = lambda a:a[2])
W = 0
edgeCount = 0


for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        W += w
        s.union(u,v)
        edgeCount += 1

if edgeCount == V - 1:
    #print("HERE",edgeCount, V-1)
    print("Connected")
    print(W)

else:
    print("Not Connected")

