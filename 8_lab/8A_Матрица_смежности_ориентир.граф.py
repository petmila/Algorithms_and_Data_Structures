fin = open('components.in', 'r')
fout = open('components.out', 'w')
n, m = map(int, fin.readline().split())
matrix = [['0']*n for i in range(n)]
for i in range(m):
    get = fin.readline().split()
    matrix[int(get[0]) - 1][int(get[1]) - 1] = '1'
for i in range(n):
    fout.write(' '.join(matrix[i]))
    fout.write('\n')
fin.close()
fout.close()