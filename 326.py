a = int(input())
x = []
z = 0
for i in range(a):
    x.append(list(map(int, input().split())))
for i in range(a):
    for j in range(i + 1, a):
        for n in range(j + 1, a):
            z = max(((x[i][0] - x[j][0])**2 + (x[i][1] - x[j][1])**2)**0.5 +
                    ((x[j][0] - x[n][0])**2 + (x[j][1] - x[n][1])**2)**0.5 +
                    ((x[n][0] - x[i][0])**2 + (x[n][1] - x[i][1])**2)**0.5
                    , z)
print(z)
