a = input()
# b = a.find('h')
# c = a.rfind('h')
# for i in range(len(a)):
#     if a[i] == 'h':
#         b = i
#         break
# for i in range(len(a) - 1, -1, -1):
#     if a[i] == 'h':
#         c = i
#         break
z = a[:a.find('h'):] + a[a.rfind('h') + 1::]
print(z)
