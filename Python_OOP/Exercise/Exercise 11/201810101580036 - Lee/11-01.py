'''
Student Name: Lee
ID: 201810101580036
Class: Network 182
'''
class Vehicle:

    def __init__(self,colour):
        self.colour=colour


# Interface
class I_air_vehicle:

    def fly(self):
        pass

# Interface
class I_land_vehicle:

    def drive(self):
        pass

class Plane(Vehicle, I_air_vehicle):

    def __init__(self, colour, air_speed):
        Vehicle.__init__(self, colour)
        self.air_speed = air_speed

    def fly(self):
        return "Plane flying"


class car(Vehicle,I_land_vehicle):

    def __init__(self,colour,land_speed):
        Vehicle.__init__(self, colour)
        self.land_speed=land_speed

    def drive(self):
        print("Car driving")


v1=Plane("red",200)
print(v1.colour)
print(v1.fly())
print(v1.air_speed)

v1=car("green",100)
print(v1.colour)
v1.drive()
print(v1.land_speed)
