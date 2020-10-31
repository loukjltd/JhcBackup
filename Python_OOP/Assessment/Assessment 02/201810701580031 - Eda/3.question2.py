# question 2
'''
Student name: Eda xiang
Student ID: 201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
class Vehicle:
    def __init__(self,name):
        self.name = name
    def go(self):
        pass
    def speed(self):
        pass

class Car(Vehicle):
    def __init__(self,name,land_speed):
        Vehicle.__init__(self,name)
        self.land_speed = land_speed
    def go(self):
        print("Drive on land at " + str(self.land_speed) + " km/h")
    def speed(self):
        return self.land_speed
class Boat(Vehicle):
    def __init__(self,name,water_speed):
        Vehicle.__init__(self,name)
        self.water_speed = water_speed
    def go(self):
        print("Drive on water " + str(self.water_speed) + " km/h")
    def speed(self):
        return self.water_speed
list1 = [Car("Ferrari",220),Car("Dodge",198),Boat("Speedboat",80),Boat("Rowboat",4)]

for l in list1:
    print(l.name)
    l.go()

total_speed = 0
average_speed = 0
max_speed = list1[0].speed()


for s in list1:
    speed1 = s.speed()
    total_speed = total_speed + speed1
    average_speed = total_speed/4
    if speed1 > max_speed:
        max_speed = speed1

print("Average speed: " + str(average_speed) +  "km/h")
print("Maximun speed: " + str(max_speed) + " km/h")