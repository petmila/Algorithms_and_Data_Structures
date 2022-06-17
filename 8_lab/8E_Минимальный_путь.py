class Pair:
    def __init__(self):
        self.path = 0
        self.name = 0
        self.status = 'not_seen'
        self.connections = []


fin = open('components.in', 'r')
fout = open('components.out', 'w')
n, m = map(int, fin.readline().split())
matrix = [Pair() for i in range(n)]
for i in range(n):
    matrix[i].name = i
# создание списков со связями
for i in range(m):
    get = fin.readline().split()
    start = int(get[0]) - 1
    end = int(get[1]) - 1
    matrix[start].connections.append(end)
    matrix[end].connections.append(start)

queue = [matrix[0]]
while queue:
    item = queue.pop(0)
    if item.status == 'seen':
        break
    item.status = 'seen'
    for next_item in matrix[item.name].connections:
        if matrix[next_item].status == 'seen':
            continue
        if matrix[next_item].path > 0:
            continue
        matrix[next_item].path = item.path + 1
        queue.append(matrix[next_item])
for item in matrix:
    fout.write(str(item.path) + ' ')

fout.close()
fin.close()