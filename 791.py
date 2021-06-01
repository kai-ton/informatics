a, b = map(int, input().split())
if (a - 1) % (b - a + 1) == 0:
    print('YES')
else:
    print('NO')
