fin = open('components.in', 'r')
fout = open('components.out', 'w')
n, m = map(int, fin.readline().split())
result = 'NO'
matrix = [['0']*n for i in range(n)]
for i in range(m):
    get = fin.readline().split()
    vertex_1 = int(get[0]) - 1
    vertex_2 = int(get[1]) - 1
    if matrix[vertex_1][vertex_2] == '0':
        matrix[vertex_1][vertex_2] = '1'
        matrix[vertex_2][vertex_1] = '1'
    else:
        result = 'YES'
fout.write(result)
fin.close()
fout.close()