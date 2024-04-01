
# relative distance of above, below, left, and right cells

adj = [(0,-1),(0,1),(-1,0),(1,0)]

def valid(r,c):
    # return True if coordinate (r,c) is not outside the matrix
    # and is not a part of a wall
    
    global steps
    
    if r >= 0 and r < 10 and c >= 0 and c < 10:
        if steps[r][c] == 0:
            return True
    return False

'''
maze:  the input maze
ends:  the list of source and destination coordinates
steps: matrix that stores the minimum number of steps from
       the source coordinate to each visited maze cell.
       = -1 if the cell is part of a wall.
'''

# Read input maze
maze = []
ends = []
for r in range(10):
    maze.append(input())
print("This is input: \n", maze)

# Set up the steps matrix
steps = [[0]*10 for r in range(10)]
print("\nSteps: \n", steps)

for r in range(10):
    for c in range(10):
        if maze[r][c] == '#':
            steps[r][c] = -1
        if maze[r][c] == 'X':
            ends.append((r,c))

print("\nSteps modified: \n", steps)
print("\nEnds: \n", ends)

# Breadth-First Search       
Queue = []
Queue.append((ends[0],0))
print("\nQueue: ", Queue, "\n")

while Queue != []:
    u = Queue[0]
    del Queue[0]

    if u[0] == ends[1]:
        print("\nEnd result: ", u[0])
        print(u[1])
        break

    for d in adj:
        r = u[0][0] + d[0]
        c = u[0][1] + d[1]
        #print("r and c: ", (r, c))

        if valid(r, c):
            v = ((r, c), u[1]+ 1)
            steps[r][c] = u[1] + 1
            Queue.append(v)
        #print("Steps: ", steps)
        #print("Queue: ", Queue, "\n")