from tools import is_pandigital
from itertools import product


mx = 0
for i in range(1, 5):
    for j in product(range(10), repeat=i):
        n = int('9' + ''.join(map(str, j)))
        
        k = 1
        s = ''
        while True:
            s += str(n * k)
            
            if len(s) > 9:
                break
            
            if is_pandigital(int(s)):
                if int(s) > mx:
                    mx = int(s)
                
            k += 1
            
print(f'Answer: {mx}')
