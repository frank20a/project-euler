from tools import divisors, is_prime


def num_prime_divisors(n):
    return len(list(filter(is_prime, divisors(n))))


i = 646
ans = []
while True:
    i += 1
    
    if num_prime_divisors(i) == 4:
        ans.append(i)
    else:
        ans = []
        
    if len(ans) == 4:
        break

print(f'Answer: {ans}')
