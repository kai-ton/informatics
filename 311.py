def x(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return x(a * a, n // 2)
    else:
        return a * x(a, n - 1)


a2, n2 = input().split()
a2 = float(a2)
n2 = int(n2)
print(x(a2, n2))
