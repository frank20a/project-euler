from tools import primes, is_prime

p = primes(1000)    # Randomly select a high limit

for i in range(len(p), 21, -1):
    for j in range(len(p)-i, 0, -1):
        n = sum(p[j: i+j])
        if n > 1000000:
            continue
        
        if is_prime(n):
            print(f'Answer: {n}')
            exit()