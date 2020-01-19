A = []
for a in range(2, 101):
    for b in range(2, 101):
        t = a**b
        if t not in A: A.append(t)
print(len(A))