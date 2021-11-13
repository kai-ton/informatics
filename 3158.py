a = list(map(int, input().split()))
b = -999999999999, 0
for i in range(len(a)):
    if a[i] > b[0]:
        b = a[i], i
print(*b)
