x = int(input())
lst = [[0] * x for i in range(x)]
a = x - 1
for i in range(x):
    for j in range(x):
        if i + j == a:
            lst[i][j] = 1
        elif i + j >= a:
            lst[i][j] = 2
for i in range(x):
    print(*lst[i])
