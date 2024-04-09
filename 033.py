from numpy import gcd

ret = []

for i in range(10, 100):
    for j in range(i + 1, 100):
        if i % 10 == 0 or j % 10 == 0:
            continue
        
        x = list(str(i))
        y = list(str(j))
        
        if x[0] in y:
            y.remove(x[0])
            x.remove(x[0])
        elif x[1] in y and x[0] != x[1]:
            y.remove(x[1])
            x.remove(x[1])
            
        if not (len(x) == 1 and len(y) == 1):
            continue
        
        if i / j == int(x[0]) / int(y[0]):
            ret.append((i, j))
            

num = 1
denum = 1

for i in ret:
    num *= i[0]
    denum *= i[1]
    
print(denum // gcd(num, denum))
