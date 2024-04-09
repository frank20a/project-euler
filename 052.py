def check(n):
    a = sorted(str(n))
    for i in range(2, 7):
        if sorted(str(n * i)) != a:
            return False
    return True

x = 0
while True:
    x += 1
    if check(x):
        print(f'Answer: {x}')
        break