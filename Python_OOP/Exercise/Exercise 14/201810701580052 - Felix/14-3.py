# Exercise 14-03
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
class Pet:
    def __init__(self,type,name,number_of_legs):
        self.name = name
        self.type = type
        self.number_of_legs = number_of_legs
f = open('.\my_pets.txt','r')
my_list = []

for line in f.readlines():
    split_line = line.split(',')
    pet_type = split_line[0]
    pet_name = split_line[1]
    pet_legs = split_line[2]
    new_pet = Pet(pet_type,pet_name,int(pet_legs))
    my_list.append(new_pet)
for obj in my_list:
 print(obj.type,": " ,obj.name,' has '+str(obj.number_of_legs)+' legs')
