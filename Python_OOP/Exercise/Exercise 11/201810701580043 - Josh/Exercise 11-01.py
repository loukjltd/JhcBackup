#Exercise 11-01
#Josh net182 201810701580043

from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self,color):
        self.color = color

class I_air_vehicle(ABC):

    @abstractmethod
    def fly(self):
        pass

class I_land_vehicle(ABC):

    @abstractmethod
    def drive(self):
        pass


class Plane(Vehicle, I_air_vehicle):

    def __init__(self, colour, air_speed):
        Vehicle.__init__(self, colour)
        self.air_speed = air_speed

    def fly(self):
        return "Plane flying"

class car(Vehicle,I_land_vehicle):
    def __init__(self,color,land_speed):
        Vehicle.__init__(self,color)
        self.land_speed = land_speed

    def drive(self):
        return "Car driving"

v1 = Plane("red",200)
print(v1.color)
print(v1.fly())
print(v1.air_speed)

v2 = car("green",100)
print(v2.color)
print(v2.drive())
print(v2.land_speed)