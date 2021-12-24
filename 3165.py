a = list(map(int, input().split()))
for i in range(len(a) // 2):
    print(a[i * 2 + 1], a[i * 2], end=' ')
if len(a) % 2 == 1:
    print(a[-1])
