x = int(input())
b = list()
a = 0
for i in range(x):
    b += [list(map(int, input().split()))]
for i in range(x):
    if a == 1:
        break
    for j in range(x):
        if b[i][j] != b[j][i]:
            print('no')
            a = 1
            break
if a == 0:
    print('yes')
