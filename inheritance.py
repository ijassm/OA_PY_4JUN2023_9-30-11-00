# Type of inheritance
# Single Inheritance.
# Multiple Inheritance.
# Multilevel Inheritance.
# Hierarchical Inheritance.
# Hybrid Inheritance.


# A Python program to demonstrate inheritance
# class Person():

#     # Constructor

#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

#     # To check if this person is an employee

#     def Display(self):
#         print(self.name, self.id)


# class Emp(Person):

#     def Print(self):
#         print("Emp class called")


# Emp_details = Emp("Mayank", 103)

# # calling parent class function
# Emp_details.Display()

# # Calling child class function
# Emp_details.Print()


# Driver code
# emp = Person("Satyam", 102)  # An Object of Person
# emp.Display()


# Python example to show the working of multiple
# inheritance


class Base1:
    def __init__(self, str):
        self.str1 = str
        print("Base1")


class Base2:
    def __init__(self, str):
        self.str2 = str
        print("Base2")


class Derived(Base1, Base2):
    def __init__(self):
        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self, "ocean")
        Base2.__init__(self, "academy")
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
