class Student:
    def __init__(self, fname, lname, cname):
        self.firstName = fname
        self.lastName = lname
        self.courseName = cname

    def getFullName(self):
        return self.firstName + " " + self.lastName


obj1 = Student("Adhi", "Narayanan", "Python")
obj2 = Student("Subik", "Shan", "Python")


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
