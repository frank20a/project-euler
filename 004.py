def isPalindrome(x):
    x = str(x)
    if len(x) % 2 == 0 and x[:int(len(x)/2)] == x[:int(len(x)/2)-1:-1] : return True
    if len(x) % 2 != 0 and x[:int(len(x)/2)] == x[:int(len(x)/2):-1] : return True
    return False

res = 0
for i in range(1000, 100, -1):
    for j in range(i,100, -1):
        t = i*j
        if isPalindrome(t):
            if t > res: res = t

print(res)