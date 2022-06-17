def Merge(array_new, start, divide, end):
    array_left = array_new[start : divide]
    array_right = array_new[divide : end]
    i = 0
    j = 0
    k = start
    while (start + i < divide and divide + j < end):
        country_1 = str(array_left[i]).split(' ')
        country_2 = str(array_right[j]).split(' ')
        if country_1[0] <= country_2[0] :
            array_new[k] = array_left[i]
            i += 1
        else:
            array_new[k] = array_right[j]
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
 
fin = open('race.in','r')
fout = open('race.out','a')
n = int(fin.readline())
array_init = []
for i in range(n):
    array_init.append(fin.readline())
 
MergeSort(array_init, 0, n)
print(array_init)
last_country = ''
for item in array_init:
    get = item.split(' ')
    country = get[0]
    name = get[1]
    if country != last_country:
        fout.write('=== ' + country + ' ===\n')
        fout.write(name)
    else:
        fout.write(name)
    last_country = country
     
fout.close()
fin.close()
