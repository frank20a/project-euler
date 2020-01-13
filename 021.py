def countDivisors(x):
    if x == 1: return 1
    c = 0
    for j in range(1, x):
        if x % j == 0: c += j
    return c

A = {}

for i in range(1, 10000):
    A[i] = countDivisors(i)

print(A)
C = []
for i in A:
    if 10000 > A[i] != i and i == A[A[i]]:
        # print(i, A[i], A[A[i]])
        if i not in C: C.append(i)
        if A[i] not in C: C.append(A[i])

print(sum(C))
print(C)