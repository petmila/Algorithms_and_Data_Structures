fin = open("quack.in", "r")
fout = open("quack.out", "w")
array_command = []
array_queue = []
array_register = [0] * 26
flags = []
intsize = 65536
results = []
 
array_command = fin.read().split()
 
for index, elem in enumerate(array_command):
    if elem[0] == ':':
        flags.append([elem[1:], index])
 
n = len(array_command)
count = 0
 
while count != n:
    command = array_command[count]
 
    if command[0] == '+':
        a = array_queue.pop(0)
        b = array_queue.pop(0)
        array_queue.append((a + b) % intsize)
 
    elif command[0] == '-':
        a = array_queue.pop(0)
        b = array_queue.pop(0)
 
        if a >= b:
            array_queue.append((a - b) % intsize)
        else:
            array_queue.append(a - b + intsize)
 
    elif command[0] == '*':
        a = array_queue.pop(0)
        b = array_queue.pop(0)
        array_queue.append((a * b) % intsize)
 
    elif command.isdigit():
        array_queue.append(int(command) % intsize)
 
    elif command[0] == '%':
        a = array_queue.pop(0)
        b = array_queue.pop(0)
 
        if b != 0:
            array_queue.append((a % b) % intsize)
        else:
            array_queue.append(0)
 
    elif command[0] == '/':
        a = array_queue.pop(0)
        b = array_queue.pop(0)
 
        if b != 0:
            array_queue.append((a // b) % intsize)
        else:
            array_queue.append(0)
 
    elif command[0] == '>':
        x = array_queue.pop(0)
        array_register[ord(command[1]) - ord('a')] = x
 
    elif command[0] == '<':
        x = array_register[ord(command[1]) - ord('a')]
        array_queue.append(x)
 
    elif command[0] == 'P':
        if len(command) == 1:
            x = array_queue.pop(0)
            results.append(str(x) + '\n')
 
        if len(command) == 2:
            x = array_register[ord(command[1]) - ord('a')]
            results.append(str(x) + '\n')
 
    elif command[0] == 'C':
        if len(command) == 1:
            x = array_queue.pop(0)
            results.append(chr(x % 256))
 
        if len(command) == 2:
            x = array_register[ord(command[1]) - ord('a')]
            results.append(chr(x % 256))
 
    elif command[0] == 'J':
        for flag in flags:
            if flag[0] == command[1:]:
                count = flag[1]
                break
 
    elif command[0] == 'Z':
        if array_register[ord(command[1]) - ord('a')] == 0:
            for flag in flags:
                if flag[0] == command[2:]:
                    count = flag[1]
                    break
 
    elif command[0] == 'E':
        if array_register[ord(command[1]) - ord('a')] == \
                array_register[ord(command[2]) - ord('a')]:
            for flag in flags:
                if flag[0] == command[3:]:
                    count = flag[1]
                    break
 
    elif command[0] == 'G':
        if array_register[ord(command[1]) - ord('a')] > \
                array_register[ord(command[2]) - ord('a')]:
            for flag in flags:
                if flag[0] == command[3:]:
                    count = flag[1]
                    break
 
    elif command[0] == 'Q':
        break
 
    count += 1
 
fout.write(''.join(results))
fin.close()
fout.close()
