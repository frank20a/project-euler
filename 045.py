import math

def isPentagonal(x):
    t = (.5 + math.sqrt(.25 + 6*x))/3
    if t.is_integer() and t > 0:
        return True
    return False

def isHexagonal(x):
    t = (1 + math.sqrt(1 + 8 * x)) / 4
    if t.is_integer() and t > 0:
        return True
    return False

i = 286
while not isHexagonal(i*(i+1)/2) or not isPentagonal(i*(i+1)/2): i += 1
print(i*(i+1)/2)