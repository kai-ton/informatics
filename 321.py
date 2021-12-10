# -1**n/(2n+1)
n = int(input())
c = 1
for i in range(1, n + 1):
    c += (-1)**i / (2 * i + 1)
print(4 * c)
