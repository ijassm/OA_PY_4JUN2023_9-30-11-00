class Student:
    firstName = ""
    lastName = ""
    courseName = ""

    def getFullName(self):
        return self.firstName + " " + self.lastName


obj1 = Student()
obj2 = Student()

obj1.firstName = "Adhi"
obj1.lastName = "Narayanan"
obj1.courseName = "Python"

obj2.firstName = "Subik"
obj2.lastName = "Shan"
obj2.courseName = "Python"

print(obj1)
print("firstname -", obj1.firstName)
print("lastName -", obj1.lastName)
print("courseName -", obj1.courseName, "\n")
print("FullName -", obj1.getFullName())
print("---------------------------")


print(obj2)
print("firstname -", obj2.firstName)
print("lastName -", obj2.lastName)
print("courseName - ", obj2.courseName, "\n")
print("FullName -", obj2.getFullName())
print("---------------------------")
