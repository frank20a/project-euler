# Power Problems:
# length of number n is N = [1 + log10(n)]
# len of 2^1000 = [1 + log10(2^1000)] = 1 + 100*log10(2) = 302

print(sum(map(int, str(2**1000))))