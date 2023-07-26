# 5 Types of Arguments in Python Function Definition:

############ default arguments.


# def person(name, location="Pondy"):
#     print(f"Myself {name}")
#     print(f"Am from {location}")


# person("Adhi", "America")
# person("Subi")

# --------------------------------------

############## keyword arguments.


# def person(name, location="Pondy"):
#     print(f"Myself {name}")
#     print(f"Am from {location}\n")


# person(location="America", name="Adhi")
# person(name="Subi")

# --------------------------------------

############### positional arguments.

# def person(name, location="Pondy"):
#     print(f"Myself {name}")
#     print(f"Am from {location}\n")


# person("Adhi", "America")
# person("Subi")

# --------------------------------------

########## arbitrary positional arguments.

# def sum(*a):
#     o = 0
#     for i in a:
#         o += i
#     return o


# print(sum())
# print(sum(2))
# print(sum(2, 4))
# print(sum(2, 7, 3))
# print(sum(2, 7, 5, 8))

# --------------------------------------

########## arbitrary keyword arguments.


# def person(**details):
#     print(f"Myself {details['name']}")
#     print(f"Am from {details['location']}\n")


# person(name="Adhi", location="America")
# person(location="UK", name="Subi")

# --------------------------------------

# a = [2, 4, 5, 7]
# b = [2, 4, 5, 7, 45, 5]


# def sum(l):
#     a = 0
#     for i in l:
#         a += i
#     return a


# print(sum(a))
# print(sum(b))
