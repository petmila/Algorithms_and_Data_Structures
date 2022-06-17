def Merge(array_new, start, divide, end):
    global inversions
    array_left = array_new[start : divide]
    array_right = array_new[divide : end]
    i = 0
    j = 0
    k = start
   
    while (start + i < divide and divide + j < end):
        if array_left[i] <= array_right[j]:
            array_new[k] = array_left[i]
            i += 1
        else:
            array_new[k] = array_right[j]
            inversions += len(array_left) - i
            j += 1
        k += 1
    if start + i < divide:
        while k < end:
            array_new[k] = array_left[i]
            i += 1
            k += 1
    else:
        while k < end:
           array_new[k] = array_right[j]
           j += 1
           k += 1
             
def MergeSort(array_new, start, end):
    if start + 1 < end:
        divide = (start + end)//2
        MergeSort(array_new, start, divide)
        MergeSort(array_new, divide, end)
        Merge(array_new, start, divide, end)
 
global inversions
inversions = 0
fin = open('inversions.in','r')
fout = open('inversions.out','w')
n = int(fin.readline())
array_init = list(map(int,fin.readline().split()))
MergeSort(array_init, 0, n)
 
fout.write(str(inversions))
fout.close()
fin.close()
