import random
def Partition(array_init, start, end):
    pivot_ind = random.randint(start, end)
    pivot = array_init[pivot_ind]
    array_init[pivot_ind], array_init[end] = array_init[end], array_init[pivot_ind]
    i = start - 1
    for j in range(start,end):
        if array_init[j] <= pivot:
            i += 1
            array_init[i], array_init[j] = array_init[j], array_init[i]
    array_init[i + 1], array_init[end] = array_init[end], array_init[i + 1]
    return i + 1
  
def QuickSort(array_init, start, end):
    if start < end:
        divide = Partition(array_init, start, end)
        QuickSort(array_init, start, divide - 1)
        QuickSort(array_init, divide + 1, end)
  
fin = open('sort.in','r')
fout = open('sort.out','w')
n = int(fin.readline())
array_init = list(map(int,fin.readline().split()))
QuickSort(array_init, 0, n - 1)
  
fout.write(' '.join(map(str, array_init)))
fout.close()
fin.close()
