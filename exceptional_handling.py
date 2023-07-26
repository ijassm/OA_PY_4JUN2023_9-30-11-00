# try:
#     a = 10
#     print(a / 0)
# except NameError:
#     print("check your variables")
# except ZeroDivisionError:
#     print("can't divide by zero")


try:
    a = int(input("enter a value A: "))
    b = int(input("enter a value B: "))
    print(a + b)
except ValueError:
    raise Exception("You can't add String with Integer")
except:
    print("Something went wrong")
else:
    print("it is perfect run without any exceptions")
finally:
    print("finally programs ends☻")
