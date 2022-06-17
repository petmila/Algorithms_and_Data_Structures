n = int(input())
array = list(map(int, input().split()))
d = [[0]*(n) for _ in range(n + 1)]
for l in range(1, n + 1):
    for i in range(n):
        j = i + l - 1
        if (j > (n - 1)):
            break
        if (i == j):
            d[i][j] = 1
        else:
            if (array[i] == array[j]):
                d[i][j] = (d[i + 1][j] + d[i][j - 1]  + 1) % 10**9
            else:
                val = d[i + 1][j] + d[i][j - 1] - d[i + 1][j - 1]
                
                d[i][j] = val % 10**9;
            
print(d[0][n - 1] % 10**9)
 

            