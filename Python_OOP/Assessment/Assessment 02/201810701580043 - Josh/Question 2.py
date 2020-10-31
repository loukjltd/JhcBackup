#Question 2
#Josh net182 201810701580043

from abc import abstractmethod as abcm

class Vehicle:
    def __init__(self, name):
        self.name = name
    @abcm
    def go(self):
        pass
    @abcm
    def speed(self):
        pass

class Car(Vehicle):
    def __init__(self, name, land_speed):
        Vehicle.__init__(self, name)
        self.land_speed = land_speed
    def go(self):
        print('Drive on land at {0} km/h'.format(self.land_speed))
    def speed(self):
        return self.land_speed

class Boat(Vehicle):
    def __init__(self, name, water_speed):
        Vehicle.__init__(self, name)
        self.water_speed = water_speed
    def go(self):
        print('Drive on water at {0} km/h'.format(self.water_speed))
    def speed(self):
        return self.water_speed

list1 = [Car('Ferrari', 220), Car('Dodge', 198), Boat('Speedboat', 80), Boat('Rowboat', 4)]
lists = []
for i in list1:
    print(i.name)
    i.go()
    lists.append(i.speed())
print('Average speed: {0} km/h'.format(sum(lists)/len(lists)))
print('Maximum speed: {0} km/h'.format(max(lists)))