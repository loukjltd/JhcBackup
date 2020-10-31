# exercise 10-04
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
class Electronic:
    def __init__(self,company):
        self.company = company
    def turn_on(self):
        return
class Smartphone(Electronic):
    def __init__(self,company,GB):
        Electronic.__init__(self,company)
        self.GB = GB
    def turn_on(self):
        print('Hold button on side')
class TV(Electronic):
    def __init__(self,company,size):
        Electronic.__init__(self,company)
        self.size = size
    def turn_on(self):
        print('Push button on remote')
e1 = Smartphone("Meizu", 64)
e2 = TV("Samsung", 50)
e1.turn_on()
e2.turn_on()


