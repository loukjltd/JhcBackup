class Car:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def details(self):
        print("{0:<4} {1:<11} {2:<7} {3}".format("Car:", self.name, "Number:", self.number))


cars = [Car("BMW", 4), Car("Volvo", 2), Car("VW", 0), Car("Saab", 8), Car("Kia", 3)]
total = 0
for i in cars:
    i.details()
    total = total+i.number
print("Total number of cars:", total)
