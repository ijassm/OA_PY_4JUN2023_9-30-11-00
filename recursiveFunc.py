a = 0


def recursiveFunc():
    global a
    a += 1
    if a <= 10:
        print(a)
        recursiveFunc()


recursiveFunc()
