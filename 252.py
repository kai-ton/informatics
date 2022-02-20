def z(n):
    if n == 0:
        return 1
    else:
        return z(n - 1) * a


a, n = map(float, input().split())
if n <= 0:
    print(float(1 / z(abs(n))))
else:
    print(float(z(n)))
