m = 0
for a in range(1, 100):
    for b in range(1, 100):
        tmp = sum(int(x) for x in str(a ** b))
        if tmp > m:
            m = tmp
            
print(f'Answer: {m}')