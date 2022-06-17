class Item:
    def __init__(self, name):
        self.name = name
        self.degree = 0
        self.status = 'not_seen'
        self.connections = []


class Matrix:
    def __init__(self, n):
        self.data = [Item(h) for h in range(n)]

    def connect(self, start, end):
        self.data[start].connections.append(end)
        self.data[end].connections.append(start)

    def degree(self):
        for item in self.data:
            item.degree = len(item.connections)
        

fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n, m = map(int, fin.readline().split())
# создание списков со связями
my_matrix = Matrix(n)
for i in range(m):
    get = fin.readline().split()
    start = int(get[0]) - 1
    end = int(get[1]) - 1
    my_matrix.connect(start, end)

my_matrix.degree()

for item in my_matrix.data:
    fout.write(str(item.degree) + ' ')
fout.close()
fin.close()