from primeTools import nextPrime, isPrime


def isTruncatablePrime(x):
    x = str(x)
    for i in range(1, len(x)):
        if not isPrime(int(x[i:])): return False
        if not isPrime(int(x[:i])): return False
    return True


A = []
t = 9
while len(A) < 11:
    t = nextPrime(t)
    if isTruncatablePrime(t): A.append(t)

print(sum(A))