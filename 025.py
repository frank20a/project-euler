n = 1
F = 1
i = 2
while F < 10**999:
    # print(i, F)
    t = F
    F += n
    n = t
    i += 1
print(i)