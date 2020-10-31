# Qusetion 2
'''
Student Name: Lee
ID: 201810101580036
Class: Network 182
'''
from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def spend(self):
        pass

class Car(Vehicle):
    def __init__(self,name,land_speed):
        Vehicle.__init__(self,name)
        self.land_speed=land_speed
    def go(self):
        print('Drive on land at {0} km/h'.format(str(self.land_speed)))

    def spend(self):
        return self.land_speed

class Boat(Vehicle):
    def __init__(self,name,water_speed):
        Vehicle.__init__(self,name)
        self.water_speed=water_speed
    def go(self):
        print('Drive on water at {0} km/h'.format(str(self.water_speed)))
    def spend(self):
        return self.water_speed

vehicle_list = [Car("Ferrari", 220), Car("Dodge", 198),
               Boat("Speedboat", 80),Boat('Rowboat', 4)]

Average_speed=0
Maximum_speed=0

for i in vehicle_list:
    print(i.name)
    i.go()
for i in vehicle_list:
    speed = i.spend()
    Average_speed += speed
    if speed > Maximum_speed:
        Maximum_speed = speed

print('Average speed: '+str(Average_speed/len(vehicle_list))+' km/h')
print('Maximum speed: '+str(Maximum_speed)+' km/h')
