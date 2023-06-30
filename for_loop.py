a = 987654321

# rev = a % 10  # 6
# a //= 10  # 53
# rev = (rev * 10) + a % 10  # 63
# a //= 10
# rev = (rev * 10) + a % 10

# print(rev)
rev = 0

l = len(str(a))

for i in range(l):
    lastNum = a % 10
    rev = (rev * 10) + lastNum
    a //= 10
    # print("lastnum", lastNum)
    # print("a", a)
    # print("rev", rev)

print(rev)
