a = int(input())
b = 0
x = list()
for i in range(a):
    x += list(map(int, input().split()))
for i in range(0, a, 2):
    for j in range(i + 2, a * 2, 2):
        if (x[j] - x[i])**2 + (x[j + 1] - x[i + 1])**2 > b:
            b = (x[j] - x[i])**2 + (x[j + 1] - x[i + 1])**2
print(b**0.5)
