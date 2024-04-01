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


# for u,v,_ in edgeList:
#     s.union(u,v)
#
# connected = True
# prev = s.findset(v)
# for v in range(V):
#     if s.findset(v) != prev:
#         print("Graph not connected")
#         connected = False
#         break
# else:
#     print("Graph Connected")



# if connected:
#     s = DisjointSets(V)
#     A = []
#     W = 0
#
#     edgeList.sort(key = lambda a:a[2])
#     for u,v,w in edgeList:
#         if s.findset(u) != s.findset(v):
#             W += w
#             A.append((u,v))
#             s.union(u,v)
#
#     print(A)
#     print(W)




#Merge both