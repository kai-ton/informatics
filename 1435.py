a = input()
if '..' in a or a[0] == '.' or a[-1] == '.':
    print(0)
else:
    a = a.split('.')
    if 0 <= int(a[0]) <= 255 and 0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255:
        print(1)
    else:
        print(0)
