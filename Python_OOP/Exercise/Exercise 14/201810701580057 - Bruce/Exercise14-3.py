'''
student name :Bruce
ID:201810701580057
class:network 182
'''

class Pet:
    def __init__(self,type,name,number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs
f = open('D:\my_pets.txt','r')
my_pets = []

for line in f.readlines():
    spilt_line = line.split(',')
    pet_types = spilt_line[0]
    pet_name = spilt_line[1]
    pet_legs = spilt_line[2]
    new_pet = Pet(pet_types,pet_name,int(pet_legs))
    my_pets.append(new_pet)

for object in my_pets:
    print(object.type + ': ' + object.name + ' has ' + str(object.number_of_legs) + ' legs')