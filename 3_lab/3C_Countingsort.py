def countingsort(array, n, index):
    array_count = [0] * 27
    for i in range(n):
        array_count[ord(array[i][index]) - 97] += 1
    for i in range(1, len(array_count)):
        array_count[i] += array_count[i - 1]
    array_result = [0] * n
    for i in range(n - 1, -1, -1):
        array_result[array_count[ord(array[i][index]) - 97] - 1] = array[i]
        array_count[ord(array[i][index]) - 97] -= 1
         
    return array_result
def radixsort(array, n, m, k):
    for i in range(m):
        if i == k:
            return array
        array = countingsort(array, n, m - i - 1)
    return array
 
fin = open('radixsort.in','r')
fout = open('radixsort.out','w')
array = []
n, m, k = map(int,fin.readline().split())
for i in range(n):
    line = fin.readline().split()
    array.append(line[0])
array = radixsort(array, n, m, k)
 
fout.write('\n'.join(array))
fout.close()
fin.close()
