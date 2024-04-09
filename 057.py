# a1 = 1 + 1/2
# a2 = 1 + 1/(2 + 1/2) = 1 + 1/(1 + a1)
# ak = 1 + 1/(1 + ak-1)

# ak = 1 + 1/(1 + nk-1 / dk-1)
# ak = (2dk-1 + nk-1) / (dk-1 + nk-1)

n = 3
d = 2
ans = 0
for i in range(1000):
    if len(str(n)) > len(str(d)):
        ans += 1
        
    # print(f'{i} - {n}/{d} = {n/d}')
    
    tmp = 2 * d + n
    d = d + n
    n = tmp
    
print(f'Answer: {ans}')