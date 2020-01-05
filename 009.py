a = 1
b = 2
c = 3
res = 0

while a+b+c != 1000:
    while b<c:
        while a<b:
            # if a**2 + b**2 == c**2: print(a, "^2 + ", b, "^2 + = ", c, "^2  ->  a+b+c = ", a + b + c)
            if a+b+c == 1000 and a**2 + b**2 == c**2:
                res = a*b*c
                break
            a += 1
        if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2: break
        b += 1
        a = 1
    if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2: break
    c += 1
    a = 1
    b = 2

print(res)