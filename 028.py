s = 1
c = 1

for i in range(3, 1002, 2):
    for j in range(4):
        c += i - 1
        s += c
        
print(f'Answer: {s}')