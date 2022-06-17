n = int(input())
array = list(map(int, input().split()))
array_subs = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i] and array_subs[j] >= array_subs[i]:
            array_subs[i] = array_subs[j] + 1
start = max(array_subs)

array_print = [0]*(start)
for i in range(n - 1, -1, -1):
    if array_subs[i] == start:
        array_print[start - 1] = (str(array[i]))
        start -= 1

print(len(array_print))
print(" ".join(array_print))
