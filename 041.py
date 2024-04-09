from tools import prev_prime


def isPandigital(x):
    a = [i for i in str(x)]
    a.sort()
    a = int(''.join(a))
    if a == int(''.join([str(i) for i in range(1, len(str(x))+1)])): return True
    return False


# pandigital numbers with 9 and 8 digits are divisible by 3 and such are not prime so the largest pandigital prime
# can at most have 7 digits
t = 7654321
while not isPandigital(t): t = prev_prime(t)
print(t)