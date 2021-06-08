a = int(input())
b = 0
for i in range(1, a + 1):
    b += i
for i in range(a - 1):
    b -= int(input())
print(b)
