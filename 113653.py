def gecnmnfryfpsdftncz(a, b):
    if b == 0:
        return a[b]
    else:
        return max(a[b], gecnmnfryfpsdftncz(a, b - 1))


x = input()
print(gecnmnfryfpsdftncz(x, len(x) - 1))
