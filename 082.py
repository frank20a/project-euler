f = open('input/p082_matrix.txt', 'r')
A = []
for line in f:
    A.append([int(i) for i in line.split(',')])


def printer(arr):
    for i in arr:
        for j in i:
            t = 2
            if j > 999: t-=1
            print(j, end=' '*t)
        print()


def solve(a):
    n = len(a)
    B = [[0 for i in range(n)] for j in range(n)]

    def solveColDown(x):
        B[0][x] = A[0][x] + B[0][x + 1]
        for i in range(1, n):
            B[i][x] = A[i][x] + min(B[i - 1][x], B[i][x + 1])

    def solveColUp(x):
        for i in range(n - 2, -1, -1):
            try:
                B[i][x] = min(B[i + 1][x] + A[i][x], B[i][x])
            except:
                print(i)

    for i in range(n): B[i][n-1] = A[i][n-1]
    for i in range(n - 2, -1, -1):
        solveColDown(i)
        solveColUp(i)

    res = float('inf')
    for i in range(n):
        if B[i][0] < res: res = B[i][0]

    return res


print(solve(A))
