from tools import divisors


def is_pandigital(n):
    return ''.join(sorted(str(n))) == '123456789'


def only_unique_digits(n):
    return len(set(str(n))) == len(str(n))


base = 10  # use decimal representation
target = 9  # searching for target-pandigital numbers
a_max = base ** ((target - 1) // 2)  # upper-bound on a

pandigitals = []
for i in range(a_max):
    if not only_unique_digits(i):
        continue
    
    if '0' in str(i):
        continue
    
    if is_pandigital(i):
        continue
    
    d = divisors(i)[1:-1]
    
    for j in range(len(d) // 2):
        if '0' in str(d[j]) or '0' in str(d[-j - 1]):
            continue
        
        if is_pandigital(int(str(d[j]) + str(d[-j - 1]) + str(i))):
            print(f'{d[j]} * {d[-j - 1]} = {i}')
            pandigitals.append(i)
            break

print(sum(pandigitals))