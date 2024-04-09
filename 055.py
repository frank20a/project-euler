from tools import is_palindrome


def is_lychrel(n):
    for _ in range(50):
        n += int(str(n)[::-1])
        if is_palindrome(str(n)):
            return False
    return True


ans = 0
for i in range(1, 10000):
    if is_lychrel(i):
        ans += 1

print(f'Answer: {ans}')