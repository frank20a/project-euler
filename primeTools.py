import numpy as np


def isPrime(n) -> bool:  # A quick O(n*sqrt(n)) implementation or isPrime
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3

    h = np.floor(1 + np.sqrt(n))
    i = 5

    while i <= h:
        if n % i == 0: return False
        if n % (i + 2) == 0: return False
        i += 6

    return True


def nPrimes(x) -> list:
    t = [2, 3]
    i = 1

    while len(t) < x:
        # All primes have a 6n+-1 form except 2 and 3
        if isPrime(6 * i - 1): t.append(6 * i - 1)
        if isPrime(6 * i + 1): t.append(6 * i + 1)
        i += 1

    return t


def nextPrime(t) -> int:
    t += 1
    while not isPrime(t): t += 1
    return t


def prevPrime(t) -> int:
    t -= 1
    while not isPrime(t): t -= 1
    return t


def primeSpace(x = 0, y = 3) -> list:
    if x < 0: x = 0

    i = 6*(int(x/6) + 1) - 1
    t = []

    if x == 3: t = [3]
    if x <= 2: t = [2, 3]

    while i <= y:
        if isPrime(i): t.append(i)
        if isPrime(i+2): t.append(i+2)
        i += 6

    if len(t) == 0: return []
    if t[-1] > y: return t[:-1]
    return t