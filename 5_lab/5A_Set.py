def hash_function(key, size):
    return key % size
 
 
def exists(array, value):
    answer = False
    for element in array:
        if element == value:
            answer = True
            break
    return answer
 
 
class Set:
    def __init__(self):
        self.size = 100000
        self.data = [[] for i in range(self.size)]
 
    def all(self, value, command):
        position = hash_function(value, self.size)
        if command == 'insert':
            if not exists(self.data[position], value):
                self.data[position].append(value)
        if command == 'exists':
            answer = exists(self.data[position], value)
            if answer:
                result.append('true')
            else:
                result.append('false')
        if command == 'delete':
            if exists(self.data[position], value):
                self.data[position].remove(value)
 
 
fin = open('set.in', 'r')
fout = open('set.out', 'w')
set_1 = Set()
commands = fin.read().split('\n')
result = []
for line in commands:
    if line == '':
        break
    get = line.split()
    set_1.all(int(get[1]), get[0])
    # print(set_1.data)
 
fout.write('\n'.join(result))
fin.close()
fout.close()
