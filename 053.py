from math import factorial


def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


ans = 0
for i in range(23, 101):
    for j in range(1, i):
        if combinations(i, j) > 1000000:
            ans += 1

print(f'Answer: {ans}')