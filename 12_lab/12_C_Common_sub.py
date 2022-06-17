x = list(map(str, input()))
y = list(map(str, input()))
 
L = [[0]*(len(y)+1) for _ in range(len(x)+1)]
for i in range(len(x)):
    for j in range(len(y)):
        if x[i] == y[j]:
            L[i][j] = L[i-1][j-1] + 1
        else:
            L[i][j] = max((L[i][j-1],L[i-1][j]))
LCS = []
i,j = len(x)-1,len(y)-1
while i >= 0 and j >= 0:
    if x[i] == y[j]:
        LCS.append(x[i])
        i, j = i-1, j-1
    elif L[i-1][j] > L[i][j-1]:
        i -= 1
    else:
        j -= 1

print("".join(LCS[::-1]))
print("\n")