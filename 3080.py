a = []
b = int(input())
c = []
q = 88888888
while b != 0:
    a.append(b)
    b = int(input())
if a[0] > a[1]:
    c.append(0)
for i in range(1, len(a) - 2):
    if a[i - 1] < a[i] > a[i + 1]:
        c.append(i)
if a[-1] > a[-2]:
    c.append(len(a) - 1)
for i in range(len(c) - 1):
    q = min(q, c[i + 1] - c[i] - 1)
if q == 88888888:
    print(0)
else:
    print(q)
