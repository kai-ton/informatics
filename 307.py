def power(a, b):
    if b == 1:
        return float(a)
    elif b == 0:
        return float(1)
    else:
        return float(a * power(a, b - 1))


z, x = map(float, input().split())
print(power(z, x))
