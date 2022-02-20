z = int(input())
x = []
for i in range(z):
    f = ' ' + input()
    e = ' ' + input()
    c = input()
    d = ' ' + input()
    c, c1 = int(c[0:-1]), c[-1]
    x.append([c, c1, f, e, d])
x.sort()
for i in range(len(x)):
    x[i][0] = str(x[i][0])
    print(*x[i][0], *x[i][1:5], sep='')
