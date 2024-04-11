import numpy as np
from itertools import permutations


def is_prime(n) -> bool:  # A quick O(n*sqrt(n)) implementation of isPrime
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    if n % 3 == 0:
        return n == 3

    h = np.floor(1 + np.sqrt(n))
    i = 5

    while i <= h:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False
        i += 6

    return True


def primes(n) -> list:
    if n == 1:
        return [2]
    if n == 2:
        return [2, 3]
    
    t = [2, 3]
    i = 1

    while len(t) < n:
        # All primes have a 6n+-1 form except 2 and 3
        if is_prime(6 * i - 1):
            t.append(6 * i - 1)
        if is_prime(6 * i + 1) and len(t) < n:
            t.append(6 * i + 1)
        i += 1

    return t


def prime_gen():
    yield 2
    yield 3

    i = 1
    while True:
        if is_prime(6 * i - 1):
            yield 6 * i - 1
        if is_prime(6 * i + 1):
            yield 6 * i + 1
        i += 1


def next_prime(t) -> int:
    t += 1
    while not is_prime(t):
        t += 1
    return t


def prev_prime(t) -> int:
    t -= 1
    while not is_prime(t):
        t -= 1
    return t


def prime_space(x=0, y=3) -> list:
    if x < 0:
        x = 0

    i = 6 * (int(x / 6) + 1) - 1
    t = []

    if x == 3:
        t = [3]
    if x <= 2:
        t = [2, 3]

    while i <= y:
        if is_prime(i):
            t.append(i)
        if is_prime(i + 2):
            t.append(i + 2)
        i += 6

    if len(t) == 0:
        return []
    if t[-1] > y:
        return t[:-1]
    return t


def divisors(n):
    t = []
    for i in range(1, int(np.sqrt(n)) + 1):
        if n % i == 0:
            t.append(i)
            if i != n // i:
                t.append(n // i)
    return sorted(t)


def common_divisors(x, y):
    return list(set(divisors(x)) & set(divisors(y)))


def is_pandigital(n, l=1, h=9):
    if l > h:
        l, h = h, l
    
    return ''.join(sorted(str(n))) == ''.join(map(str, range(l, h + 1)))


def pandigitals(h=9, l=1, inv=False):
    p = list(permutations(range(l, h + 1)))[::-1 if inv else 1]
    for i in p:
        yield int(''.join(map(str, i)))


def is_composite(n):
    return len(divisors(n)) > 2


def is_palindrome(n):
    return str(n) == str(n)[::-1]
