a = int(input())
z = a // 60
# print(a, (a + 19) // 20 * 230)
if a == 0 or (a + 19) // 20 * 230 > 440:
    z += (z + a + 59) // 60
    print(0, 0, 0, 0, z)
else:
    x = a // 20
    a %= 20
    if a == 0 or (a + 9) // 10 * 125 > 230:
        x = (x + a + 19) // 20
        print(0, 0, 0, x, z)
    else:
        c = a // 10
        a %= 10
        if a == 0 or (a + 4) // 5 * 70 > 125:
            c = (c + a + 9) // 10
            print(0, 0, c, x, z)
        else:
            v = a // 5
            if a == 0 or a * 15 > 70:
                v = (v + a + 4) // 5
                print(0, v, c, x, z)
            else:
                a %= 5
                print(a, v, c, x, z)
