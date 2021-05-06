def min(a, b, c, d):
    e = a
    if e > b:
        e = b
    if e > c:
        e = c
    if e > d:
        e = d
    return e

a, b, c, d = list(map(int, input().split()))
print(min(a, b, c, d))
