import math
f = open('p042_words.txt', 'r')
a = [i.strip('"') for i in f.read().split(',')]


def isTriangle(x):
    t = -.5 + math.sqrt(.25 + 2*x)
    if t.is_integer() and t > 0: return True
    return False


def getVal(x):
    t = 0
    for i in x: t += ord(i) - 64
    return t


res = 0;
for i in a:
    if isTriangle(getVal(i)): res += 1

print(res)
