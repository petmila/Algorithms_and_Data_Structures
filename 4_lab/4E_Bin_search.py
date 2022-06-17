fin = open('binsearch.in', 'r')
fout = open('binsearch.out', 'w')
n = int(fin.readline())
array = list(map(int, fin.readline().split()))
m = int(fin.readline())
get = list(map(int, fin.readline().split()))
for x in get:
    l_left = -1
    l_right = n
    r_right = n
    r_left = -1
    while (l_right - l_left > 1) or (r_right - r_left > 1):
        l_middle_index = (l_left + l_right) // 2
        r_middle_index = (r_right + r_left) // 2
        if r_right - r_left > 1:
            if array[r_middle_index] > x:
                r_right = r_middle_index
            else:
                r_left = r_middle_index
        if l_right - l_left > 1:
            if array[l_middle_index] >= x:
                l_right = l_middle_index
            else:
                l_left = l_middle_index
    if l_right < n and array[l_right] == x:
        fout.write(str(l_right + 1) + ' ' + str(r_right) + '\n')
    else:
        fout.write('-1 -1' + '\n')
fin.close()
fout.close()
