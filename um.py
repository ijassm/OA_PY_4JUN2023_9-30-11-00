def add(l):
    a = 0
    for i in l:
        a += i
    return a


def product(l):
    a = 1
    for i in l:
        if i != 0:
            a *= i
    return a
