a, b = map(int, input().split())
x = []
for j in range(a):
    x.append([])
    for i in range(b):
        x[j].append(0)
for i in range(a):
    for j in range(b):
        if i == 0 or j == 0:
            x[i][j] = 1
        else:
            x[i][j] = x[i][j - 1] + x[i - 1][j]
[print(*i) for i in x]
