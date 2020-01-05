def check(x):
    t = 0
    tn = 0

    for i in range(2, 21):
        if x % i >= t and x % i != 0:
            t = x % i
            tn = i

    return tn

res = 1
temp = check(res)

while temp != 0:
    res *= temp
    temp = check(res)

print (res)