def get_independent_set(u): 
    if d[u] != -1:
        return d[u]      
    not_u_sum = 0
    with_u_sum = 0
    for i in matrix[u]:
        not_u_sum += get_independent_set(i)
        for j in matrix[i]:
            with_u_sum += get_independent_set(j)
    d[u] = max(1 + with_u_sum, not_u_sum)
    return d[u]

n = int(input())
matrix = [[] for i in range (n + 1)]
for i in range(1, n + 1):
    parent = int(input())
    matrix[parent].append(i)

d = [-1]*(n + 1)
print(get_independent_set(matrix[0][0]))

