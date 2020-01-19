# Haven't proven an upper limit for this but eyeballing it to 99999 and going up from there (999999 got me right answer)
A = []
for i in range(10, 999999):
    a = [int(j) for j in str(i)]
    if sum([j**5 for j in a]) == i: A.append(i)
print(sum(A))