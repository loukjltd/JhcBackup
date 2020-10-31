from abc import ABC, abstractmethod


class Vehicle:
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def speed(self):
        pass


class Car(Vehicle):
    def __init__(self, name, land_speed):
        Vehicle.__init__(self, name)
        self.land_speed = land_speed

    def go(self):
        print("Drive on land at %s km/h" % self.land_speed)

    def speed(self):
        return self.land_speed


class Boat(Vehicle):
    def __init__(self, name, water_speed):
        Vehicle.__init__(self, name)
        self.water_speed = water_speed

    def go(self):
        print("Drive on water at %s km/h" % self.water_speed)

    def speed(self):
        return self.water_speed


transport_list = [Car("Ferrari", 220), Car("Dodge", 198), Boat("Speedboat", 80), Boat("Rowboat", 4)]

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
print("Average speed: %s km/h" % str(total/a))
print("Maximum speed: %s km/h" % str(maximum))

