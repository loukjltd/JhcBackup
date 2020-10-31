#
'''
class:net182
name:lenny
ID:201810701580045
'''

from abc import ABC


class Vehicle:

    def __init__(self,colour):
        self.colour = colour


class I_air_vehicle(ABC):

    def fly(self):
        pass


class I_land_vehicle(ABC):

    def driver(self):
        pass


class Plane(Vehicle, I_air_vehicle):

    def __init__(self, colour, air_speed):
        Vehicle.__init__(self, colour)
        self.air_speed = air_speed

    def fly(self):
        return "Plane flying"


class Car(Vehicle, I_land_vehicle):

    def __init__(self, colour, land_speed):
        Vehicle.__init__(self,colour)
        self.land_speed = land_speed

    def drive(self):
        return "Car driving"


v1 = Plane('red',200)
print(v1.colour)
print(v1.fly())
print(v1.air_speed)

v1 = Car('green',100)
print(v1.colour)
print(v1.drive())
print(v1.land_speed)