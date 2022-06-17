fin = open('components.in', 'r')
fout = open('components.out', 'w')
n = int(fin.readline())
result = 'YES'
matrix = [['0']*n for i in range(n)]
for i in range(n):
    get = fin.readline().split()
    for j in range(n):
        matrix[i][j] = get[j]
        # проверка нулей на главной диагонали
        if (i == j) and (matrix[i][j] != '0'):
            result = 'NO'
# проверка симметричности
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            result = 'NO'
fout.write(result)
fin.close()
fout.close()