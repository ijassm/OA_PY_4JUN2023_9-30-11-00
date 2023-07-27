l1 = [2, 4, 6, 7, 8]
l2 = [5, 9, 10]


# def double(l):
#     a = []
#     for i in l:
#         a.append(i * 2)
#     return a


# def triple(l):
#     a = []
#     for i in l:
#         a.append(i * 3)
#     return a


# def quadruple(l):
#     a = []
#     for i in l:
#         a.append(i * 4)
#     return a


# def pentuple(l):
#     a = []
#     for i in l:
#         a.append(i * 5)
#     return a


# print("double")
# print(double(l1))
# print(double(l2), "\n")

# print("triple")
# print(triple(l1))
# print(triple(l2), "\n")

# print("quadruple")
# print(quadruple(l1))
# print(quadruple(l2), "\n")

# print("pentuple")
# print(pentuple(l1))
# print(pentuple(l2), "\n")

mapDouble1 = map(lambda i: i * 2, l1)
mapDouble2 = map(lambda i: i * 2, l2)

print(list(mapDouble1), "mapDouble1")
print(list(mapDouble2), "mapDouble2\n")


def myMap(func, iterable):
    l = []
    for i in iterable:
        l.append(func(i))
    return l


def fun(i):
    return i * 2


myMapDouble1 = myMap(lambda i: i * 2, l1)
myMapDouble2 = myMap(fun, l2)

myMapTriple1 = myMap(lambda i: i * 3, l1)
myMapTriple2 = myMap(fun, l2)

print(myMapDouble1, "myMapDouble1")
print(myMapDouble2, "myMapDouble2")
