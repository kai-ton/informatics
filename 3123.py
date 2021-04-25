a = input()
for i in range(len(a)):
    if a[i] == 'h':
        b = i
        break
for i in range(len(a) - 1, -1, -1):
    if a[i] == 'h':
        c = i
        break
z = a[:b:] + a[c:b:-1] + a[c::]
print(z)

