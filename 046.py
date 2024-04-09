from tools import is_composite, next_prime


i = 0
while True:
    i += 1
    n = 2 * i + 1
    
    if not is_composite(n):
        i += 1
        continue
    
    prime = 7
    while True:
        j = 1
        while True:
            p = prime + 2 * j**2
            if p >= n:
                break
            j += 1
            
        if p == n:
            print(f'{n} = {prime} + 2 * {j}^2')
            break
            
        if prime > n:
            print(f'\n\nAnswer: {n}')
            exit()
            
        prime = next_prime(prime)