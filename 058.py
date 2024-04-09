from tools import is_prime


c = 1
p = 0
i = 0
n = 1
while True:
    i += 1
    for _ in range(4):
        c += 1
        n += 2 * i
        if is_prime(n):
            p += 1
    
    print(f'{i * 2 + 1}: {p}/{c}={p / c}')
    if p / c < 0.1:
        break
    
print(f'Answer: {i * 2 + 1}')