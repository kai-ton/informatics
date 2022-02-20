a = int(input())
z = 0
x = 0
while a != 0:
    if x == 0:
        z += 1
        x = z
    x -= 1
    a -= 1
    print(z, end=' ')
