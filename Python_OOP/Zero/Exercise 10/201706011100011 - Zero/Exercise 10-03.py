#  net171 ZhaoYinTing

from abc import ABC, abstractmethod

class Vehicle:                                              #<Make an abstract class called Vehicle>
    def __init__(self, name, number_of_wheels):
        self.name = name
        self.number_of_wheels = number_of_wheels

    @abstractmethod                                          #<Make an abstract method called display_vehicle(). Use pass>
    def display_vehicle(self):
        pass



class Car(Vehicle):
     def __init__(self, name, number_of_wheels, number_of_doors):
         Vehicle.__init__(self, name, number_of_wheels)
         self.number_of_doors = number_of_doors

     def display_vehicle(self):
         print("{0} has {1} wheels and {2} doors".format(self.name, self.number_of_wheels, self.number_of_doors))


class Bike(Vehicle):                                        #<Make a class called Bike that inherits vehicle>
    def __init__(self, name, number_of_wheels, type):       #<Make the __init__ method that calls the Vehicle __init__ method>
        Vehicle.__init__(self, name, number_of_wheels)      #<It also has the parameter type>
        self.type = type

    def display_vehicle(self):                              #<Override the display_vehicle() method. Make it say "??? has ?? wheels and is a ??? bike>
        print("{0} has {1} wheels and is a {2} bike.".format(self.name, self.number_of_wheels, self.type))


#<Make an object called v1 from the Car class with name="Car", number of wheels = 4 and number of doors = 4>
v1=Car("Car",4,4)
#<Make an object called v2 from the Bike class with name="Bike", number of wheels = 2 and type = "mountain">
v2=Bike("Bike",2,"mountain")
#<Call the display_vehicle() method on v1>
v1.display_vehicle()
# <Call the display_vehicle() method on v2>
v2.display_vehicle()