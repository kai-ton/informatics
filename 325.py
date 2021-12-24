a = int(input())
x = list()
c = list()
for i in range(a):
    x.append(list(map(int, input().split())))
for i in range(len(x)):
    c.append(((x[i][0]**2 + x[i][1]**2), x[i][0], x[i][1]))
c.sort()
for i in range(len(c)):
    print(c[i][1], c[i][2])
