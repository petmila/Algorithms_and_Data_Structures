fin = open("search1.in", 'r')
fout = open("search1.out", 'w')
p = list(map(str, fin.readline()))
t = list(map(str, fin.readline()))
p = p[:len(p) - 1]
answer = []
for i in range(len(t) - len(p) + 1):
    if p == t[i :i + len(p)]:
        answer.append(str(i + 1))
fout.write(str(len(answer)) + '\n')
fout.write(' '.join(answer))
fin.close()
fout.close()