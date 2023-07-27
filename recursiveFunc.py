# a = 0


# def recursiveFunc():
#     global a
#     a += 1
#     if a <= 10:
#         print(a)
#         recursiveFunc()


# recursiveFunc()


# Task

# sum(2)() => 2
# sum(2)(4)() => 6
# sum(2)(4)(3)() => 9


def sum(a):
    return lambda b: lambda c: a + b + c


print(sum(2)(3)(4)(5))
