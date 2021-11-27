a = input()
b, c = map(int, input().split())
b, c = b - 1, c - 1
print(f'{a[0:b]}{a[b:c + 1][::-1]}{a[c + 1:]}')
