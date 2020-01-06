import primeTools as pt
from itertools import permutations, combinations

A = pt.primeSpace(1000, 10000)


def checkDist(L):
    if abs(L[0]-L[1]) == abs(L[1]-L[2]):
        return True
    return False

res = []
for i in A:
    c = 0
    t = []
    for j in permutations(str(i)):
        k = int(''.join(j))
        if k > 1000 and pt.isPrime(k) and k not in t:
            c += 1
            t.append(k)
    if c >= 3:
        t.sort()
        for l in combinations(t, 3):
            if checkDist(l) and l not in res: res.append(l)

res = [''.join(map(str, i)) for i in res]
print(res)