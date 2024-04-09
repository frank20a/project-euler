from tools import pandigitals


divs = [2, 3, 5, 7, 11, 13, 17]

ans = []
for i in pandigitals(9, 0):
    tmp = 0
    for j, d in enumerate(divs):
        if int(str(i)[j + 1: j + 4]) % d == 0:
            tmp += 1
        else:
            break
    
    if tmp == 7:
        ans.append(int(i))
        
print(f'Answer: {sum(ans)} - {ans}')