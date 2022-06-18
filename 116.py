def MinDigit(n, x=999999999999999999999):
    while n != 0:
        if n % 10 < x:
            x = n % 10
        n //= 10
    return x


def MaxDigit(n, x=0):
    while n != 0:
        if n % 10 > x:
            x = n % 10
        n //= 10
    return x


z = int(input())
print(MinDigit(z), MaxDigit(z))
