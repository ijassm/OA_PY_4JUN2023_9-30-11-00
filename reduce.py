from functools import reduce

l = [2, 4, 5, 6]


# def func(accumulator, currentValue):
#     print(accumulator, "accumulator")
#     print(currentValue, "currentValue\n")
#     return accumulator * currentValue


sum = reduce(lambda acc, value: acc + value, l, 5)

print(sum)
