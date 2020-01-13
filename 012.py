def countDivisors(x):
    c = 1
    for j in range(int(x/2) + 1, 1, -1):
        if x % j == 0: c += 1
        if c > 500: break
    print(x, c)
    if c > 500: return True
    return False


i = 2
t = 1
while not countDivisors(t):
    t += i
    i += 1
print(i)