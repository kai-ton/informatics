a = int(input())
b = int(input())
n = int(input())
c = b * n // 100
b = b * n - c * 100
print(a * n + c, b)
