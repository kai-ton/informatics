a = [0, 0, 0]
x = int(input())
a[2] += x // 60
x %= 60
if x > 34:
    a[2] += 1
else:
    a[1] += x // 10
    x %= 10
    if x > 8:
        a[1] += 1
    else:
        a[0] += x
print(*a)
