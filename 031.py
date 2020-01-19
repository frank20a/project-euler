# Using DP
A = {0: [0], 1: [1], 2: [1], 5: [1], 10: [1], 20: [1], 50: [1], 100: [1], 200: [1]}

for i in range(1, 201):
    A[0].append(0)
    # print()
    for j in range(1, len(A)):
        # print(i, list(A.keys())[j], end = " ")
        if list(A.keys())[j] > i:
            # print("NO", A[list(A.keys())[j-1]][i])
            A[list(A.keys())[j]].append(A[list(A.keys())[j-1]][i])
        else:
            # print("YE", A[list(A.keys())[j-1]][i], A[list(A.keys())[j]][i-list(A.keys())[j]])
            A[list(A.keys())[j]].append(A[list(A.keys())[j-1]][i] + A[list(A.keys())[j]][i-list(A.keys())[j]])

print(A[200][200])
