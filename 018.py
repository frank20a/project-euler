import graphslib as gl

A = '\
75,\
95 64,\
17 47 82,\
18 35 87 10,\
20 04 82 47 65,\
19 01 23 75 03 34,\
88 02 77 73 07 63 67,\
99 65 04 28 06 16 70 92,\
41 41 26 56 83 40 80 70 33,\
41 48 72 33 47 32 37 16 94 29,\
53 71 44 65 25 43 91 52 97 51 14,\
70 11 33 28 77 73 17 78 39 68 17 57,\
91 71 52 38 17 14 91 43 58 50 27 29 48,\
63 66 04 68 89 53 67 30 73 16 69 87 40 31,\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

A = A.split(',')
A = [list(map(int, i.split(" "))) for i in A]
A.reverse()
for i in range(1, len(A)):
    for j in range(len(A[i])):
        A[i][j] += max(A[i-1][j], A[i-1][j+1])

print(A[-1])

'''
root = gl.Node(0)
end = gl.Node(s+1)
G = gl.WeightedGraph(root)

# fill the Graph with nodes
for i in range(1, s+1):
    G.addNode(gl.Node(i))

# make the connections
for i in range(len(A) - 1):
    print(i, A[i])
    for j in range(len(A[i])):
        print("Node ", pos(i, j))
        G.addVertex(pos(i, j), pos(i+1, j), -A[i][j], False)
        G.addVertex(pos(i, j), pos(i + 1, j + 1), -A[i][j], False)

print(A[-1])
for i in range(len(A[-1])):
    print("Node ", pos(len(A)-1, i))
    G.addVertex(pos(len(A)-1, i), s, -A[-1][i], False)

# By adding the negative of the weight we can use the standard dijkstra algorithm to find the shortest path
# and then reverse the distance to get the absolute value.
shortestDist, path = G.dijkstra(0, s)
print(-shortestDist)
for i in path: print(i)
'''