def hash_function(key, size):
    num = 0
    for i in range(len(key) - 1, 0, -1):
        num += ord(key[i])*i
    return num % size
 
 
def exists_key(array, key):
    answer = None
    for element in array:
        if element.key == key:
            answer = element
            break
    return answer
 
 
class Member():
    def __init__(self):
        self.key = None
        self.value = None
 
 
class Map():
    def __init__(self):
        self.size = 10000
        self.data = [[Member()] for i in range(self.size)]
 
    def all(self, key_value, value, command):
        position = hash_function(key_value, self.size)
        if command == 'put':
            member = exists_key(self.data[position], key_value)
            if member is None:
                member = Member()
                member.key = key_value
                member.value = value
                self.data[position].append(member)
            elif member is not None:
                member.value = value
        if command == 'get':
            answer = exists_key(self.data[position], key_value)
            if answer is None:
                result.append('none')
            else:
                result.append(answer.value)
        if command == 'delete':
            answer = exists_key(self.data[position], key_value)
            if answer is not None:
                self.data[position].remove(answer)
 
 
fin = open('map.in', 'r')
fout = open('map.out', 'w')
map_1 = Map()
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
