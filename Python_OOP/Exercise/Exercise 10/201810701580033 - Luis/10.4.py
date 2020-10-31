# exercise 10-04
'''
student name: Luis
ID: 201810701580033
class: network182
'''

class Electronic:
    def __init__(self,company):
        self.company=company
    def turn_on(self):
            return 2

class Smartphone(Electronic):
    def __init__(self,company,GB):
        Smartphone.__company = company
        self.GB=GB
    def turn_on(self):
        print("Hold button on side")

class TV(Electronic):
    def __init__(self,company,size):
        Smartphone.__company = company
        self.size=size
    def turn_on(self):
        print("Push button on remote")

e1 = Smartphone("Meizu", 64)
e2 = TV("Samsung", 50)
e1.company="Meizu"
e1.GB=64
e2.company="Samsung"
e2.size=50
e1.turn_on()
e2.turn_on()
