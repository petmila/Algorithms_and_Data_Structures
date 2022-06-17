global prev_for_all
global next_for_all
global position_for_all
next_for_all = None
position_for_all = 0
prev_for_all = None
 
 
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
        self.prev = None
        self.next = None
 
 
class LinkedMap():
    def __init__(self):
        self.size = 10000
        self.data = [[Member()] for i in range(self.size)]
 
    def all(self, key_value, value, command):
        global prev_for_all
        global position_for_all
        global next_for_all
        position = hash_function(key_value, self.size)
        if command == 'put':
            member = exists_key(self.data[position], key_value)
            if member is None:
                member = Member()
                member.prev = prev_for_all
                member.key = key_value
                member.value = value
                if len(self.data) > 0:
                    self.data[position_for_all][len(self.data[position_for_all]) - 1].next = member
                self.data[position].append(member)
                prev_for_all = member
                next_for_all = member
                position_for_all = position
            elif member is not None:
                member.value = value
        if command == 'next':
            member = exists_key(self.data[position], key_value)
            if member is None:
                result.append('none')
            elif member.next is None:
                result.append('none')
            else:
                result.append(member.next.value)
        if command == 'prev':
            member = exists_key(self.data[position], key_value)
            if member is None:
                result.append('none')
            elif member.prev is None:
                result.append('none')
            else:
                result.append(member.prev.value)
        if command == 'get':
            answer = exists_key(self.data[position], key_value)
            if answer is None:
                result.append('none')
            else:
                result.append(answer.value)
        if command == 'delete':
            answer = exists_key(self.data[position], key_value)
            if answer is not None:
                if answer.next is not None:
                    answer.next.prev = answer.prev
                if answer.prev is not None:
                    answer.prev.next = answer.next
                    if answer == prev_for_all:
                        prev_for_all = answer.prev
                        position_for_all = hash_function(answer.prev.key, self.size)
                if answer.prev is None and answer.next is None:
                    next_for_all = None
                    position_for_all = 0
                    prev_for_all = None
                self.data[position].remove(answer)
 
 
 
fin = open('linkedmap.in', 'r')
fout = open('linkedmap.out', 'w')
map_1 = LinkedMap()
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
