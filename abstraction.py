from abc import ABC, abstractmethod

# Python program demonstrate
# abstract base class work


class Car(ABC):
    @abstractmethod
    def mileage(self):
        print("abstract method")


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")


# Driver

# c = Car()

# print(c)

t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()

d = Duster()
d.mileage()
