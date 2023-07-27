a = [134, 43, 56, 2, 3, 5, 6, 32, 65, 123]


def func(i):
    if i > 20:
        return True
    return False


f = filter(func, a)

print(list(f))
