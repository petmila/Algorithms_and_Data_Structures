fin = open('knapsack.in','r')
fout = open('knapsack.out', 'w')
s, n = map(int,fin.readline().split())
weights = list(map(int, fin.readline().split()))
d = [[0]*(s + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, s + 1):
        if j >= weights[i - 1]: 
            d[i][j] = max(d[i -1][j], d[i - 1][j - weights[i - 1]] + weights[i - 1])
        else:
            d[i][j] = d[i - 1][j]

fout.write(str(d[n][s]))
fin.close()
fout.close()