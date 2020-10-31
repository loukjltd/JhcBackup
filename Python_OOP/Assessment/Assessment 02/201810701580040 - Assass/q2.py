'''
class:net182
name:Assass
id:201810710580040
'''
from abc import abstractmethod
class vehicle:
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def speed(self):
        pass
class car(vehicle):
    def __init__(self,name,land_speed):
        vehicle.__init__(self,name)
        self.land_speed=land_speed
    def go(self):
        print('Drive on land at '+ str(self.land_speed) +' km/h')
    def speed(self):
        return self.land_speed
class boat(vehicle):
    def __init__(self,name,water_speed):
        vehicle.__init__(self,name)
        self.water_speed=water_speed
    def go(self):
        print('Drive on land at '+ str(self.water_speed) +' km/h')
    def speed(self):
        return self.water_speed
l = [car("Ferrari", 220), car("Dodge", 198),boat("Speedboat", 80),boat('Rowboat', 4)]
t=0
m=0
for i in l:
    print(i.name)
    i.go()
    t+=i.speed()
    if i.speed() >=m:
        m=i.speed()
print('Average speed: '+str('%.1f' %(t/len(l)))+' km/h')
print('Maximum speed: '+str(m)+' km/h' )

