res = {i: 0 for i in range(1, 1001)}

for a in range(1, 1001):
    for b in range(a, 1001):
        c = (a**2 + b**2)**0.5
        if c != int(c):
            continue
        
        if a + b + c <= 1000:
            res[int(a + b + c)] += 1
            
print(f'Answer: {max(res, key=res.get)}')