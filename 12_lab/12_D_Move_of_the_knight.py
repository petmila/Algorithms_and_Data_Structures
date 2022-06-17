def step(i, j):
    if i >= 0 and j >= 0 and i < n and j < m:
        if array[i][j] == -1:
            array[i][j] = step(i-2, j-1) + step(i-2, j+1) + step(i-1, j-2) + step(i+1, j-2)
    else:
        return 0
    return array[i][j]
    
fin = open('knight2.in','r')
fout = open('knight2.out', 'w')
n, m = map(int,fin.readline().split())
array = [[-1]*(m) for i in range(n)]
array[0][0] = 1
fout.write(str(step(n-1, m-1)))
fin.close()
fout.close()