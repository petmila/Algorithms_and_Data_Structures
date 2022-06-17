def Heapify(array, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < n and int(array[left]) > int(array[i]):
        largest = left
    if right < n and int(array[right]) > int(array[largest]):
        largest = right
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        Heapify(array, largest, n)
def Build_Heap(array, n):
    for i in range(n // 2, -1, -1):
        Heapify(array, i, n)
def Heapsort(array, n):
    Build_Heap(array, n)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        n -= 1
        Heapify(array, 0, n)
fin = open('sort.in','r')
fout = open('sort.out','w')
n = int(fin.readline())
array = list(map(str,fin.readline().split()))
Heapsort(array, n)
 
fout.write(' '.join(array))
fout.close()
fin.close()
