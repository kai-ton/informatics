x = input().split()
a, b = map(int, input().split())
x.append(0)
for i in range(len(x) - 1, a, -1):
    x[i] = x[i - 1]
x[a] = b
print(*x)
