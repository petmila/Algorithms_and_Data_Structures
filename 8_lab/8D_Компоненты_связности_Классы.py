class Item:
    def __init__(self, name):
        self.path = 0
        self.name = name
        self.component = 0
        self.status = 'not_seen'
        self.connections = []


class Matrix:
    def __init__(self, n):
        self.data = [Item(h) for h in range(n)]
        self.array = [h for h in range(n)]

    def connect(self, start, end):
        self.data[start].connections.append(end)
        self.data[end].connections.append(start)

    def width_round(self):
        queue = []
        k = 1
        for this in self.array:
            if self.data[this].component == 0:
                queue.append(self.data[self.array[this]])
                while queue:
                    item_see = queue.pop(0)
                    if item_see.status == 'seen':
                        break
                    item_see.status = 'seen'
                    item_see.component = k

                    for next_item in self.data[item_see.name].connections:
                        if self.data[next_item].status == 'seen':
                            continue
                        if self.data[next_item].path > 0:
                            continue
                        self.data[next_item].path = item_see.path + 1
                        queue.append(self.data[next_item])
                k += 1
        return k - 1


fin = open('components.in', 'r')
fout = open('components.out', 'w')
n, m = map(int, fin.readline().split())
# создание списков со связями
my_matrix = Matrix(n)
for i in range(m):
    get = fin.readline().split()
    start = int(get[0]) - 1
    end = int(get[1]) - 1
    my_matrix.connect(start, end)

result = my_matrix.width_round()
fout.write(str(result) + '\n')

for item in my_matrix.data:
    fout.write(str(item.component) + ' ')
# fout.write(' '.join(components))
fout.close()
fin.close()
