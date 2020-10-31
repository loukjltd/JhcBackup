# Assessment 2 Question 2
"""
Student Name: Sean
ID: 201810701580042
Class: Network 182
"""


from abc import ABC


class Vehicle(ABC):

    def __init__(self, name):
        self.name = name

    def go(self):
        pass

    def speed(self):
        pass


class Car(Vehicle):

    def __init__(self, name, land_speed):
        Vehicle.__init__(self, name)
        self.land_speed = land_speed

    def go(self):
        print('Drive on land at ' + str(self.land_speed) + ' km/h')

    def speed(self):
        return self.land_speed


class Boat(Vehicle):

    def __init__(self, name, water_speed):
        Vehicle.__init__(self, name)
        self.water_speed = water_speed

    def go(self):
        print('Drive on land at ' + str(self.water_speed) + ' km/h')

    def speed(self):
        return self.water_speed


transport_list = [Car('Ferrari', 220), Car('Dodge', 198), Boat('Speedboat', 80), Boat('Rowboat', 4)]

total = 0
maximum = 0
a = 0
for i in transport_list:
    print(i.name)
    i.go()
    a += 1
    total += i.speed()
    if maximum < i.speed():
        maximum = i.speed()
print('Average speed: ' + str(total / a) + ' km/h')
print('Maximum speed: ' + str(maximum) + ' km/h')
