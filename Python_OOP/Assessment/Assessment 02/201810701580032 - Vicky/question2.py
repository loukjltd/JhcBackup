from abc import ABC, abstractmethod
import math
class Vehicle(ABC):
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def go(self):
        pass
    def speed(self):
        pass

class Car(Vehicle):
    def __init__(self,name,land_speed):
        Vehicle.__init__(self,name)
        self.land_speed = land_speed
    def go(self):
        print("Drive on land at {0} km/h".format(self.land_speed))
    def speed(self):
        return self.land_speed

class Boat(Vehicle):
    def __init__(self,name,water_speed):
        Vehicle.__init__(self, name)
        self.water_speed = water_speed
    def go(self):
        print("Drive on water at {0} km/h".format(self.water_speed))
    def speed(self):
        return self.water_speed

list = [Car("Ferrari",220),Car("Dodge",198),Boat("Speedboat",80),Boat("Rowboat",4)]
sum = 0
for i in list:
    print(i.name)
    i.go()
total_speed = 0
max_speed = list[0].speed()
for a in list:
    speed1 = a.speed()
    total_speed = total_speed + speed1
    if speed1 > max_speed:
        max_speed = speed1

average_speed = (total_speed/len(list))
print("Average speed:",str(average_speed),"km/h")
print("Maximum speed:",str(max_speed),"km/h")