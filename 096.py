class Num:
    def __init__(self, n):
        self.n = n
        if n == 0:
            self.p = list(range(1, 10))
            self.solved = False
        else:
            self.p = [n]
            self.solved = True

    def update(self):
        global c
        if len(self.p) == 1:
            print("-",self.p, '-', end ='')
            self.n = self.p[0]
            self.solved = True
            c += 1

    def check(self, n):
        if n in self.p: self.p.remove(n)
        self.update()

    def __str__(self):
        return str(self.n)


def getSquare(x, y):
    return (x // 3, y // 3)


def isSolved():
    global A
    for i in A:
        for j in i:
            if not j.solved: return False
    return True


def checkRow(x, num):
    print("Checking Row ", x)
    global A
    for i in range(9):
        t = A[x][i]
        print(t, end = '')
        if t.n != 0: num.check(t.n)
    print()


def checkCol(y, num):
    print("Checking Col ", x)
    global A
    for i in range(9):
        t = A[i][y]
        print(t, end='')
        if t.n != 0: num.check(t.n)
    print()


def checkSquare(x, y, num):
    print("Checking Sqr ", x, y)
    global A
    x, y = getSquare(x, y)
    for i in range(3):
        for j in range(3):
            t = A[3*x + i][3*y + j]
            print(t, end='')
            if t.n != 0: num.check(t.n)
    print()


def printBoard():
    global A
    for i in A:
        for j in i:
            print(j, end='  ')
        print()
    print()


f = open('input/p096_sudoku.txt', 'r')

for kwlos in range(50):
    A = []
    print(f.readline())

    for i in range(9):
        A.append([Num(int(j)) for j in f.readline()[:9]])
    printBoard()

    c = 1
    while not isSolved():
        if c > 0:
            c = 0
            t = []
            for x in range(9):
                for y in range(9):
                    if not A[x][y].solved:
                        checkRow(x, A[x][y])
                        checkCol(y, A[x][y])
                        checkSquare(x, y, A[x][y])
            printBoard()
        else:
            print("No Changes")
            input()
    input()