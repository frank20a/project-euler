from primeTools import isPrime


def quad(a, b, n):
    return n ** 2 + a * n + b


def maxN(a, b):
    n = 0
    while isPrime(quad(a, b, n)): n += 1
    return n


m = 0
for i in range(-1000, 1000):
    for j in range(-1000, 1000):
        t = maxN(i, j)
        if t > m:
            m = t
            mA = i
            mB = j

print(mA * mB)
