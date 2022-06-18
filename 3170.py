a = list(map(int, input().split()))
x = 0
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            x += 1
print(x)
