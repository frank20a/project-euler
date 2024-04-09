from math import factorial as fact
from itertools import product

# 7 x 9! = 2540160 < 9999999 < 8 x 9! = 2903040 so we can limit the search to 7 digits

ans = []
for i in range(2, 8):
    for j in product(range(10), repeat=i):
        if j[0] == 0:
            continue
        
        s = sum(fact(k) for k in j)
        if s == int(''.join(map(str, j))):
            ans.append(s)
            
print(f'Answer: {ans} = {sum(ans)}')
