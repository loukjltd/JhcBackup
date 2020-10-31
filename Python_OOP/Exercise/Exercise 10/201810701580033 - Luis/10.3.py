
# exercise 10-03
'''
student name: Luis
ID: 201810701580033
class: network182
'''

from abc import ABC, abstractmethod

class Vehicle:
   def __init__(self, name, number_of_wheels):
      self.name = name
      self.number_of_wheels = number_of_wheels

def display_vehicle():
    return 2

class Car(Vehicle):
    def __init__(self, name, number_of_wheels, number_of_doors):
        Vehicle.__init__(self, name, number_of_wheels)
        self.number_of_doors = number_of_doors

    def display_vehicle(self):
        print("{0} has {1} wheels and {2} doors".format(self.name, self.number_of_wheels, self.number_of_doors))

class Bike ():
     def __init__(self,name, number_of_wheels,type):
          Vehicle.__init__(self, name, number_of_wheels)
          self.type=type
     def display_vehicle(self):
             print("{0} has {1} wheels is a {2} bike".format(self.name, self.number_of_wheels, self.type))


v1=Car("Car", 4,4 )
v2=Bike("Bike", 2 ,"mountain" )
v1.name="Car"
v1.number_of_wheels=4
v1.number_of_wheels=4
v2.name="Bike"
v2.number_of_wheels=2
v2.type="mountain"

v1.display_vehicle()
v2.display_vehicle()

