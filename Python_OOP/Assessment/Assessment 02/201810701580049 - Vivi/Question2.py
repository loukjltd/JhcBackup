#Question 2
"""
class:net182
name:vivi
id:201810701580049
"""
from abc import abstractmethod

class Vehicle:
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def speed(self):
        pass

class Car(Vehicle):
    def __init__(self,name,land_speed):
        Vehicle.__init__(self,name)
        self.land_speed = land_speed

    def go(self):
        return ("Drive on land at {} km/h".format(self.land_speed))

    def speed(self):
        return self.land_speed

class Boat(Vehicle):
    def __init__(self,name,water_speed):
        Vehicle.__init__(self,name)
        self.water_speed = water_speed

    def go(self):
        return ("Drive on water at {} km/h".format(self.water_speed))
    def speed(self):
        return self.water_speed

Vehicle_list = [Car("Ferrari",220),Car("Dodge",198),
                Boat("Speedboat",80),Boat("Rowboat",4)]

num = 0
max = []
for info in Vehicle_list:

    print(info.name)
    print(info.go())
    num += info.speed()
    max.append(info.speed())
Maximum = 0
for i in max:
    if i == 0:
        Maximum = i
    else:
        if i > Maximum:
            Maximum = i
        else:
            Maximum =Maximum

print("Average speed: {} km/h ".format(num/len(Vehicle_list)))
print("Maximum speed: {} km/h ".format(Maximum))
exit(0)