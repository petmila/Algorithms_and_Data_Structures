fin = open('garland.in', 'r')
fout = open('garland.out', 'w')
n, A = map(float, fin.readline().split())
n = int(n)
left = 0
right = A
garland = [0] * n
garland[0] = A
while right - left > 0.000001:
    state = 1
    garland[1] = (right + left) / 2
    for i in range(2, n):
        garland[i] = 2 * garland[i - 1] - garland[i - 2] + 2
        if garland[i] < 0:
            state = 0
            break
    if state == 1:
        right = garland[1]
    else:
        left = garland[1]
fout.write(str(int(garland[n - 1]*100)/100))
fin.close()
fout.close()
