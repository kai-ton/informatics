n, m = map(int, input().split())
x = list()
b = 0, 0, 0
for i in range(n):
    x += [list(map(int, input().split()))]
for i in range(n):
    a = 0, 0, i
    for j in range(m):
        a = max(a[0], x[i][j]), a[1] + x[i][j], i
    if a[0] > b[0]:
        b = a
    elif a[0] == b[0] and a[1] > b[1]:
        b = a
print(b[2])
