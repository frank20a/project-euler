num = ["", 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
ten = ['', 'teen', 'twenty', 'thirty','forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
spe = ['hundredand', 'thousand']


def toStr(x):
    if x <= 19: return num[x]

    t = ''
    if x < 100:
        t += ten[int(x/10)] + toStr(x%10)
    elif x < 1000:
        t += toStr(int(x/100)) + spe[0] + toStr(x%100)
    elif x < 1000000:
        t += toStr(int(x/1000)) + spe[1] + toStr(x%1000)
    return t


res = 0
for i in range(1, 1001):
    res += len(toStr(i))

print(res)