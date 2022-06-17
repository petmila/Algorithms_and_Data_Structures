from bisect import bisect_left
n = int(input())
array = list(map(int, input().split()))
array_pos = [1]*(1+ n)
array_len = [10**9]*(1+ n)
array_prev = [0]*(1+ n)
array_len[0] = -10**9
array_pos[0] = -1
len = 0
for i in range(n):
    j = bisect_left(array_len, array[i])
    if array_len[j - 1] < array[i] and array[i] < array_len[j]:
        array_len[j] = array[i]
        array_pos[j] = i
        array_prev[i] = array_pos[j - 1]
        len = max(len, j)

start = array_pos[len]
array_print = ['']*len
print(len)
while start != -1:
    array_print[len - 1] = str(array[start])
    start = array_prev[start]
    len -= 1

print(" ".join(array_print))
