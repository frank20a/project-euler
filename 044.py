import math


def genPenta(n):
    return [int(i*(3*i-1)/2) for i in range(1, n)]


def isPentagonal(x):
    t = (.5 + math.sqrt(.25 + 6*x))/3
    if t.is_integer() and t > 0: return True
    return False


A = genPenta(100000)
for i in A:
    for j in A[A.index(i) :: -1]:
        if isPentagonal(i+j) and isPentagonal(abs(i-j)):
            print(abs(i-j))
