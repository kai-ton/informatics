a = list(input())
b = list()
for i in range(len(a) - 1):
    if a[i] != ' ' or a[i + 1] != ' ':
        b.append(a[i])
if a[-1] != ' ':
    print(*b, a[-1], sep='')
else:
    print(*b, sep='')
