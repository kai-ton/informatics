z = int(input())
a = 1
b = 2
x = 3
while z > b:
    a, b = b, a + b
    x += 1
if z == b:
    print(x)
else:
    print(-1)
