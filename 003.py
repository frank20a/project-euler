import primeTools as pt


def largestPrimeFactor(a):
    primes = [1]
    while a != 1 and not pt.isPrime(a):
        if a % 2 == 0:
            a = int(a/2)
        else:
            t = 3
            while a % t != 0: t = pt.nextPrime(t)
            a = int(a/t)
            primes.append(t)
    if pt.isPrime(a): primes.append(a)
    return max(primes)


print(largestPrimeFactor(600851475143 ))
