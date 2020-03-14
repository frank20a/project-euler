f = open('./input/p081_matrix.txt', 'r')
A = []
for line in f:
    A.append([int(i) for i in line.split(',')])


def solve(a):
    n = len(a)
    B = [[0 for i in range(n)] for j in range(n)]

    def calc(x, y):
        if x == 79:
            B[x][y] = B[x][y + 1] + A[x][y]
        elif y == 79:
            B[x][y] = B[x + 1][y] + A[x][y]
        else:
            B[x][y] = min(B[x + 1][y], B[x][y + 1]) + A[x][y]

    B[n-1][n-1] = A[n-1][n-1]

    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            calc(i, j)
            calc(j, i)
            calc(i, i)

    return B[0][0]


print(solve(A))
