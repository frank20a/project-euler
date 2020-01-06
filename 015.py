# from permutation theory we know that we have 2 groups (down and right) of 20 obj with a total of 2*20=40 obj so
# N = (2*20)!/20^2!

from math import factorial
n = 3
print(int(factorial(2*n)/(factorial(n))**2))