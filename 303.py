# korova korovy korov
a = int(input())
if a % 10 == 1 and a != 11:
    print(a, 'korova')
elif a % 10 == 2 and a != 12 or a % 10 == 3 and a != 13 or a % 10 == 4 and a != 14:
    print(a, 'korovy')
else:
    print(a, 'korov')
