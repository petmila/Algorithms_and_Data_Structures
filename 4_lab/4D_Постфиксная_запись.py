fin = open('postfix.in', 'r')
fout = open('postfix.out', 'a')
array = ['']*100
for i in range(100):
    array[i] = ''
get = fin.readline().split()
top = -1
for command in get:
    if command == '+':
        one = int(array[top])
        array[top] = 0
        top -= 1
        two = int(array[top])
        array[top] = int(two + one)
    elif command == '-':
        one = int(array[top])
        array[top] = 0
        top -= 1
        two = int(array[top])
        array[top] = int(two - one)
    elif command == '*':
        one = int(array[top])
        array[top] = 0
        top -= 1
        two = int(array[top])
        array[top] = int(two * one)
    else:
        top += 1
        array[top] = int(command)
fout.write(str(array[top]))
fin.close()
fout.close()
