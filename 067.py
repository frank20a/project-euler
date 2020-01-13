file = open('p067_triangle.txt', 'r')
A = file.readlines()
A = [list(map(int, i[:-1].split(' '))) for i in A]
A.reverse()
for i in range(1, len(A)):
    for j in range(len(A[i])):
        A[i][j] += max(A[i-1][j], A[i-1][j+1])

print(A[-1])
