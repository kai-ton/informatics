a = int(input())
b = int(input())
if a <= 0:
    x = 0
else:
    x = int(a**0.5)
if x**2 < a:
    x += 1
while x**2 <= b:
    print(x**2, end=' ')
    x += 1
