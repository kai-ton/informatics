a = float(input())
b = float(input())
c = float(input())
eps = 0.00000001
if abs(a + b - c) <= eps:
    print('YES')
else:
    print('NO')
