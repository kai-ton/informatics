a = int(input())
z, x = 0, 1
for i in range(a):
    z, x = x, z + x
print(x)
