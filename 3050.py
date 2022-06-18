def move(n, a, b):
    if n == 0:
        pass
    else:
        move(n - 1, a, 6 - a - b)
        print(n, a, b)
        move(n - 1, 6 - a - b, b)


move(1000, 1, 3)

