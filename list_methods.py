a = []

a.append(1)
a.append(2)
# a.pop()
b = a
c = a.copy()

b[0] = 0


print(a)
print(b)
print(c)

# print(id(a))
# print(id(b))
# print(id(c))
