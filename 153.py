def ad(n):
    if n <= 2:
        return 1
    else:
        return ad(n - 1) + ad(n - 2)


a = int(input())
if a == 0:
    print(0)
else:
    print(ad(a))
