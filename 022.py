f = open('p022_names.txt', 'r')


def toNums(a):
    t = []
    for i in a:
        t.append(ord(i) - 64)
    return sum(t)


x = [i.strip('"') for i in f.read().split(',')]
x.sort()
x = [toNums(i) for i in x]
c = 0
for i in range(len(x)): c += (i + 1) * x[i]
print(c)