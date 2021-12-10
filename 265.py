a = int(input())
b = int(input())
c = int(input())
x = max(c // a, 1) * 2 * b
if 1 > c // a:
    print(x)
elif c % a == 0:
    print(x)
elif c % a <= a // 2:
    print(x + b)
else:
    print(x + b * 2)
