n = int(input())
a = []
z = 0
x = 0
c = 0
for i in range(n):
    a += input().split()
for i in range(2, len(a), 5):
    z += int(a[i])
for i in range(3, len(a), 5):
    x += int(a[i])
for i in range(4, len(a), 5):
    c += int(a[i])
print(z / n, x / n, c / n)
