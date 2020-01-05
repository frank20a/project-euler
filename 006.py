n = list(range(1, 101))

sq = lambda x: x**2
res = (len(n) * (n[0] + n[-1]) / 2)**2 - sum([sq(i) for i in n])

print(res)