from operator import itemgetter, attrgetter, methodcaller
 
class Item:
    def __init__(self, name):
        self.name = name
        self.status = 0
 
fin = open('spantree3.in', 'r')
fout = open('spantree3.out', 'w')
n, m = map(int, fin.readline().split())
matrix = [Item(i) for i in range(n)]
edges = []
 
for i in range(m):
    get = fin.readline().split()
    x = int(get[0]) - 1
    y = int(get[1]) - 1
    if x != y and int(get[2]) != 0:
        edges.append((matrix[x], int(get[2]), matrix[y]))
        
edges = sorted(edges, key=itemgetter(1), reverse=True)  
chosen_one = edges[len(edges) - 1]
index = len(edges) - 1
edges.pop(index)
summ = chosen_one[1]
chosen_one[0].status = 1
chosen_one[2].status = 1
len_array = 1
while (len_array < n - 1):
    for i in range(len(edges) - 1, -1, -1):
        if (edges[i][0].status == 0 and edges[i][2].status == 1) or (edges[i][0].status == 1 and edges[i][2].status == 0) :
            chosen_one = edges[i]
            index = i
            summ += chosen_one[1]
            chosen_one[0].status = 1
            chosen_one[2].status = 1
            break
    edges.pop(index)   
    len_array += 1
    
fout.write(str(summ))
fout.close()
fin.close()