def task1():
    isl = ord(input("Input symbol:"))
    if ord('a') <= isl <= ord('z') or ord('A') <= isl <= ord('Z'):
        print("This english letter %s and her code %s" % (chr(isl), isl))
    else:
        print("This other symbol %s and his code %s" % (chr(isl), isl))
    pass


def task2():
    try:
        a = int(input("Input numb: "))
    except ValueError:
        print("It's not numb, try again")
    else:
        fl = 0
        if a >= 0:
            fl = 1
            for i in range(1, a+1):
                fl *= i
            print("Your faktorial:", fl)
    pass


def task3():
    for a in range(1, 11):
        for b in range(1, 11):
            print("%5d" % (a * b), end='')
        print()
    pass
