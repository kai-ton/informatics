from math import factorial
b = int(input())
a = int(input())
print(int(factorial(b) / (factorial(a) * factorial(b - a))))
