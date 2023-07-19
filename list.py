l = [13, 72, 34, 44, 5, 6, 743]

# mutable
l[-1] = 0

print(l)
print(l[0], "0 index")
print(l[1], "1 index")
print(l[5], "5 index")
# Negative Index
print(l[-1], "-1 index")
print(l[-2], "-2 index")
print(l[-3], "-3 index")

print(type(l))

# method

l.append(1234)
print(l, "l")
l.pop()
print(l, "l")

print("String\n")

s = "hello      ocean"

# immutable
# s[0] = "i"

print(s)
print(s[0], "0 index")
print(s[-1], "-1 index")
print(len(s), "len")
