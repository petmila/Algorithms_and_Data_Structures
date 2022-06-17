fin = open('antiqs.in','r')
fout = open('antiqs.out','w')
n = int(fin.readline())
array_init = []
for i in range(1,n+1):
    array_init.append(i)
 
for i in range(2,n):
    array_init[i], array_init[i // 2] = array_init[i // 2], array_init[i]
   
fout.write(' '.join(map(str, array_init)))
fout.close()
fin.close()
