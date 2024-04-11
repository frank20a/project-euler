from tools import is_prime, next_prime, primes
from itertools import combinations


def check_set(prime_set):
    for a, b in combinations(prime_set, 2):
        if not is_prime(int(str(a) + str(b))) or not is_prime(int(str(b) + str(a))):
            return False
    return True


def create_prime_set(N, prev=None) -> set:
    
    if N == 1:
        if type(prev) is list:
            try:
                prev = prev[0]
            except IndexError:
                prev = None
        s = set([next_prime(prev) if prev is not None else 2])
        # print(f'N: {N}, prev: {prev}, s: {sorted(list(s))}')
        return s
    else:
        while True:
            if prev is None:
                prev = primes(N)
                s = set(prev)
            else:
                print(f'')
                s = create_prime_set(N - 1, prev[:-1]) | set([prev[-1]])
                
            print(f'N: {N}, prev: {prev}, s: {sorted(list(s))}', end='')                
                                
            if len(s) != N:
                s = set(primes(N - 1)) | create_prime_set(1, sorted(list(s))[-1])
                print(f' -> {sorted(list(s))}', end='')
                
            prev = sorted(list(s))
            if check_set(s):
                return s
            
            print()
                

print(f'Answer: {create_prime_set(4)}')
