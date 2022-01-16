# import math
# a = int(input())
# b = 1
# for i in range(1, a + 1):
#     b += 1 / math.factorial(i)
# print(b)
a = int(input())
b = 1
c = 1
for i in range(1, a + 1):
    c /= i
    b += c
print(b)
