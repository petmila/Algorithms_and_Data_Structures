fin = open('queue.in', 'r')
fout = open('queue.out', 'a')
n = int(fin.readline())
array = [0]*(n)
tail = -1
head = 0
for i in range(n):
    get = fin.readline().split(' ')
    command = str(get[0])
    if command == '+':
        meaning = get[1].split('\n')
        tail += 1
        array[tail] = int(meaning[0])
 
    else:
        fout.write(str(array[head]) + '\n')
        head += 1
fin.close()
fout.close()
