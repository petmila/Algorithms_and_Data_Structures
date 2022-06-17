fin = open('stack.in', 'r')
fout = open('stack.out', 'a')
n = int(fin.readline())
array = [0]*(n)
top = -1
for i in range(n):
    get = fin.readline().split(' ')
 
    command = str(get[0])
    if command == '+':
        meaning = get[1].split('\n')
        top += 1
        array[top] = int(meaning[0])
 
    else:
        fout.write(str(array[top]) + '\n')
        top -= 1
fin.close()
fout.close()
