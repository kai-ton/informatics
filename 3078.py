a = list()
c = int(input())
b = list()
e = 0
while c != 0:
    a.append(c)
    c = int(input())
for i in range(1, len(a)):
    if a[i - 1] > a[i]:
        b.append(1)
    elif a[i - 1] < a[i]:
        b.append(-1)
    else:
        b.append(0)
print(b)
d = [1, b[0]]
for i in range(len(b)):
    if d[1] == b[i] and b[i] != 0:
        d[0] += 1
    else:
        if e < d[0]:
            e = d[0]
            d = [1, b[i + 1]]
        else:
            d = [1, b[i + 1]]
    print(e, d)


print(max(e, d[0]))
