def hash_function(key, size):
    num = 0
    for i in range(len(key) - 1, -1, -1):
        num += ord(key[i])*(i + 1)
    return num % size
 
 
def exists_key(array, key):
    answer = None
    for element in array:
        if element.key == key:
            answer = element
            break
    return answer
 
 
def exists_value(array, value):
    answer = None
    for element in array:
        if element == value:
            answer = element
            break
    return answer
 
 
class Map():
    def __init__(self):
        self.size = 100
        self.key = None
        self.data = [[] for i in range(self.size)]
 
    def put(self, value):
        position = hash_function(value, self.size)
        member = exists_value(self.data[position], value)
        if member is None:
            self.data[position].append(value)
 
    def get(self):
        local_result = []
        index = 0
        local_result.append(str(index))
        for element in self.data:
            for value in element:
                local_result.append(value)
                index += 1
        local_result[0] = str(index)
        result.append(' '.join(local_result))
 
    def delete(self, value):
        position = hash_function(value, self.size)
        answer = exists_value(self.data[position], value)
        if answer is not None:
            self.data[position].remove(answer)
 
 
class MultiMap():
    def __init__(self):
        self.size = 5000
        self.data = [[Map()] for i in range(self.size)]
 
    def all(self, key_value, value, command):
        position = hash_function(key_value, self.size)
        if command == 'put':
            search = exists_key(self.data[position], key_value)
            if search is None:
                map = Map()
                map.key = key_value
                map.put(value)
                self.data[position].append(map)
            else:
                search.put(value)
 
        if command == 'get':
            answer = exists_key(self.data[position], key_value)
            if answer is None:
                result.append('0')
            else:
                answer.get()
        if command == 'delete':
            search = exists_key(self.data[position], key_value)
            if search is not None:
                search.delete(value)
        if command == 'deleteall':
            answer = exists_key(self.data[position], key_value)
            if answer is not None:
                self.data[position].remove(answer)
 
fin = open('multimap.in', 'r')
fout = open('multimap.out', 'w')
map_1 = MultiMap()
commands = fin.read().split('\n')
result = []
for line in commands:
    if line == '':
        break
    get = line.split()
    if len(get) > 2:
        map_1.all(get[1], get[2], get[0])
    else:
        map_1.all(get[1], 'no', get[0])
fout.write('\n'.join(result))
fin.close()
fout.close()
