from tools import next_prime, is_prime


def isTruncatablePrime(x):
    x = str(x)
    for i in range(1, len(x)):
        if not is_prime(int(x[i:])): return False
        if not is_prime(int(x[:i])): return False
    return True


A = []
t = 9
while len(A) < 11:
    t = next_prime(t)
    if isTruncatablePrime(t): A.append(t)

print(sum(A))