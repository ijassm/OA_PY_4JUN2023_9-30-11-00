# Example 1: Polymorphism in addition operator

# num1 = 1
# num2 = 2
# print(num1+num2)

# ---

# str1 = "hello"
# str2 = "ocean"

# print(str1 + " " + str2)

# ---------------------------------------------


# Function Polymorphism in Python
# Example 2: Polymorphic len() function

# print(len("Programiz"))
# print(len(["Python", "Java", "C"]))
# print(len({"Name": "John", "Address": "Nepal"}))

# ---------------------------------------------

# Class Polymorphism in Python
# Example 3: Polymorphism in Class Methods

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Bark")


# cat1 = Cat("Kitty", 2.5)
# dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
#     animal.make_sound()
#     animal.info()
#     animal.make_sound()


# ---------------------------------------------


# Polymorphism and Inheritance
# Example 4: Method Overriding


from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length
        
    #method overiding
    def area(self):
        return self.length**2

    #method overiding
    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi * self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

# ---------------------------------------------
