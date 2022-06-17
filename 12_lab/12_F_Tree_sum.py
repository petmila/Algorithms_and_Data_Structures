def get_independent_set(u): 
    if d[u[0]] != -1:
        return d[u[0]]
    not_u_sum = 0
    with_u_sum = 0
    for i in matrix[u[0]]:
        not_u_sum += get_independent_set(i)
        for j in matrix[i[0]]:
            with_u_sum += get_independent_set(j)
    d[u[0]] = max(u[1] + with_u_sum, not_u_sum)
    return d[u[0]]

fin = open('selectw.in','r')
fout = open('selectw.out', 'w')
n = int(fin.readline())
matrix = [[] for i in range (n + 1)]
for i in range(1, n + 1):
    parent, value = map(int, fin.readline().split())
    matrix[parent].append((i, value))

d = [-1]*(n + 1)
answer = get_independent_set(matrix[0][0])
fout.write(str(answer))
fin.close()
fout.close()
