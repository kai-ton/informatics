n, m = map(int, input().split())
for i in range(n):
    if i % 2 == 0:
        for j in range(0, m):
            print(f'{(i * m + j): 3}', end='')
        print()
    else:
        for j in range(m - 1, -1, -1):
            print(f'{(i * m + j): 3}', end='')
        print()
