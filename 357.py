n, m = map(int, input().split())
b = 0, 0, 0
for i in range(n):
    x = list(map(int, input().split()))
    for j in range(m):
        if x[j] > b[0]:
            b = x[j], i, j
print(b[0])
print(b[1], b[2])
