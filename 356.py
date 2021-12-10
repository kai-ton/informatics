n, m = map(int, input().split())
b = 0
x = 0
for i in range(n):
    c = sum(map(int, input().split()))
    if c > b:
        b = c
        x = i
print(b)
print(x)
