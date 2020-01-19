A = {}
A[1] = 1
A[89] = 89


def squarer(x):
    x = [int(i)**2 for i in str(x)]
    return sum(x)


def check(x):
    global A
    if x in A.keys():
        return A[x]
    else:
        t = check(squarer(x))
        A[x] = t
        return t


res = 0
for i in range(1, 10000000):
    if i%300000 == 0: print(i/100000, "%")
    if check(i) == 89: res += 1
print(res)