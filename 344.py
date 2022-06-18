a = input()
x = 1
s = 0
for i in a[::-1]:
    if i == '1':
        s += x
    x *= 2
print(s)
