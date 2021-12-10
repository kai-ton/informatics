a = input().split()
b = 1
for i in range(len(a) - 1):
    if a[i] != a[i + 1]:
        b += 1
print(b)
