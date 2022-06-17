fin = open('brackets.in', 'r')
fout = open('brackets.out', 'a')
n = 500
for i in range(n):
    array = [''] * (10**4)
    top = -1
    state = 'YES'
    get = fin.readline()
    if not get:
        break
    for input in get:
        if state == 'NO':
            break
        last = array[top]
        if input == ')':
            if last == '(':
                top -= 1
            else:
                fout.write('NO' + '\n')
                state = 'NO'
        elif input == ']':
            if last == '[':
                top -= 1
            else:
                fout.write('NO' + '\n')
                state = 'NO'
        else:
            top += 1
            array[top] = input
    if top != 0 and state == 'YES':
        fout.write('NO' + '\n')
        state = 'NO'
    if state == 'YES':
        fout.write('YES'+ '\n')
 
fin.close()
fout.close()
