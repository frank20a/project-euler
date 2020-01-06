from time import *
start_time = time()

A = {}


def next(n):
    if n % 2 == 0: return int(n/2)
    return 3*n + 1


def calc(n):
    global A

    if n == 1:
        return 1
    elif n in A.keys():
        return A[n]
    else:
        A[n] = calc(next(n)) + 1
        return A[n]


m = 0
mn = 0
for i in range(1, 1000000):
    t = calc(i)
    if t > m:
        print(i, t)
        m = t
        mn = i

print(time() - start_time)