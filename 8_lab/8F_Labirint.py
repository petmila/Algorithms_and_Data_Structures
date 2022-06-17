class Item:
    def __init__(self, name):
        self.path = 0
        self.name = name
        self.status = 'not_seen'
        self.life = 'dead'
        self.neighbours = []
        self.direction = ''


class Neighbour:
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n, m = map(int, fin.readline().split())
matrix = [['']*m for i in range(n)]
for i in range(n):
    get = fin.readline()
    for j in range(m):
        matrix[i][j] = get[j]
start = 0
end = 0
graph = [Item(i) for i in range(n*m)]
count = -1
# создание графа из доступных вершин со списками доступный соседей и направлений к ним
for i in range(n):
    for j in range(m):
        count += 1
        if matrix[i][j] != '#':
            graph[count].life = 'alive'
            if matrix[i][j] == 'S':
                start = count
            if matrix[i][j] == 'T':
                end = count
        else:
            continue
        if 0 <= i + 1 < n:
            if matrix[i+1][j] != '#':
                new_neighbour = Neighbour(count + m, 'D')
                graph[count].neighbours.append(new_neighbour)

        if 0 <= i - 1 < n:
            if matrix[i-1][j] != '#':
                new_neighbour = Neighbour(count - m, 'U')
                graph[count].neighbours.append(new_neighbour)

        if 0 <= j + 1 < m:
            if matrix[i][j + 1] != '#':
                new_neighbour = Neighbour(count + 1, 'R')
                graph[count].neighbours.append(new_neighbour)

        if 0 <= j - 1 < m:
            if matrix[i][j - 1] != '#':
                new_neighbour = Neighbour(count - 1, 'L')
                graph[count].neighbours.append(new_neighbour)
#for i in graph:
 #   print(i.name)
  #  for k in i.neighbours:
   #     print(k.name, k.direction)
queue = [graph[start]]
state = 'do'
while queue and state == 'do':
    item = queue.pop(0)
    if item.status == 'seen':
        break
    item.status = 'seen'
    for next_item in graph[item.name].neighbours:

        if graph[next_item.name].status == 'seen':
            continue
        if graph[next_item.name].path > 0:
            continue
        graph[next_item.name].path = item.path + 1
        graph[next_item.name].direction = item.direction + next_item.direction
        if graph[next_item.name].name == end:
            state = 'break'
        queue.append(graph[next_item.name])

if state == 'do':
    fout.write('-1')
else:
    fout.write(str(len(graph[end].direction))+'\n')
#print(str(len(graph[end].direction)))
    fout.write(str(graph[end].direction))
#print(str(graph[end].direction))
fout.close()
fin.close()