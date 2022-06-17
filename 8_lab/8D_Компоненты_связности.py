class Item:
    def __init__(self, name):
        self.path = 0
        self.name = name
        self.component = 0
        self.status = 'not_seen'
        self.connections = []


fin = open('components.in', 'r')
fout = open('components.out', 'w')
n, m = map(int, fin.readline().split())
matrix = [Item(i) for i in range(n)]
array = [i for i in range(n)]
# создание списков со связями
for i in range(m):
    get = fin.readline().split()
    start = int(get[0]) - 1
    end = int(get[1]) - 1
    matrix[start].connections.append(end)
    matrix[end].connections.append(start)

queue = []
components = [0] * n
k = 1  # счетчик компонентов
for this in array:
    if matrix[this].component == 0:
        queue.append(matrix[array[this]])
        while queue:
            item = queue.pop(0)
            if item.status == 'seen':
                break
            item.status = 'seen'
            item.component = k
            components[item.name] = str(k)
            for next_item in matrix[item.name].connections:
                if matrix[next_item].status == 'seen':
                    continue
                if matrix[next_item].path > 0:
                    continue
                matrix[next_item].path = item.path + 1
                queue.append(matrix[next_item])
        k += 1

fout.write(str(k - 1) + '\n')
# for item in matrix:
#   fout.write(str(item.component) + ' ')
fout.write(' '.join(components))
fout.close()
fin.close()