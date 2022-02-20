n = list(map(int, input().split()))
mi = n.index(min(n))
ma = n.index(max(n))
b = n
b[ma], b[mi] = b[mi], b[ma]
print(*b)
