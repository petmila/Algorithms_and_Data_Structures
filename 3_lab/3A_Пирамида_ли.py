def Heapify(array, i):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i
    if left < len(array) and array[left] < array[i]:
        smallest = left
        return 'NO'
    if right < len(array) and array[right] < array[smallest]:
        smallest = right
        return 'NO' 
    return 'YES'
 
fin = open('isheap.in','r')
fout = open('isheap.out','w')
n = int(fin.readline())
array = list(map(int,fin.readline().split()))
answer = 'YES'
for i in range(n // 2):
    answer = Heapify(array, i)
    if answer == 'NO':
        break
fout.write(answer)
fout.close()
fin.close()
