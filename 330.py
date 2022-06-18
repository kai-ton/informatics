a = int(input())
x = []
for i in range(a):
    x.append(input().split())
    for j in range(-1, -4, -1):
        x[i][j] = int(x[i][j])
z = [-1]
for i in range(a):
    if z[0] < x[i][2] + x[i][3] + x[i][4]:
        z = [x[i][2] + x[i][3] + x[i][4], i]
    elif z[0] == x[i][2] + x[i][3] + x[i][4]:
        z.append(i)
for i in z[1::]:
    print(*x[i][:2:])
