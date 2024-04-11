from tools import divisors


def types(n):
    s = sum(divisors(n)[:-1])
    return [s < n, s == n, s > n]


def sum_abundands(n):
    tmp = set()
    abundant = []
    
    for i in range(n + 1):
        t = types(i)
        if t[2]:
            abundant.append(i)
            
            for j in abundant[:-1]:
                tmp.add(i + j)
            tmp.add(i * 2)
                
    ret = set(range(n)) - tmp
    
    return sum(ret)


print(sum_abundands(28123))
