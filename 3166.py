a = list(map(int, input().split()))
# x = a[-1]
# for i in range(len(a) - 1, 0, -1):
#     a[i] = a[i-1]
# a[0] = x
a.insert(0, a.pop())
print(*a)
