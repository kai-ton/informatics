a = int(input())
b = 0
c = 0, 0
for i in range(a):
    x = list(map(int, input().split()))
    if (x[0]**2 + x[1]**2) > b:
        b = (x[0]**2 + x[1]**2)
        c = x
print(*c)
