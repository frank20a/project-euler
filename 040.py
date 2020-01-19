a = ''
i = 1
while len(a) < 1000000:
    a += str(i)
    i += 1

res = 1
for i in range(7):
    res *= int(a[10**i - 1])
print(res)