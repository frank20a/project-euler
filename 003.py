import tools as pt


def largestPrimeFactor(a):
    primes = [1]
    while a != 1 and not pt.is_prime(a):
        if a % 2 == 0:
            a = int(a/2)
        else:
            t = 3
            while a % t != 0: t = pt.next_prime(t)
            a = int(a/t)
            primes.append(t)
    if pt.is_prime(a): primes.append(a)
    return max(primes)


print(largestPrimeFactor(600851475143 ))
