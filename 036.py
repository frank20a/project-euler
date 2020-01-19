def isPalindrome(x):
    if len(x) % 2 == 0 and x[:int(len(x)/2)] == x[:int(len(x)/2)-1:-1] : return True
    if len(x) % 2 != 0 and x[:int(len(x)/2)] == x[:int(len(x)/2):-1] : return True
    return False

res = 0
for i in range(1000000):
    if isPalindrome(str(i)) and isPalindrome(str(bin(i))[2:]): res += i

print (res)