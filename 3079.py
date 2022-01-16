a = []
b = int(input())
c = 0
while b != 0:
    a.append(b)
    b = int(input())
for i in range(0, len(a) - 2):
    if a[i] < a[i + 1] > a[i + 2]:
        c += 1
print(c)
