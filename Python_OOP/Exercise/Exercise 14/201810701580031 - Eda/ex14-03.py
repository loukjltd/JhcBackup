# exercise 14-03
'''
student name: Eda
ID: 201810701580031
class: network182
'''
class Pet:
    def __init__(self,type,name,number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs
f = open("./my_pets.txt","r")
my_pets = []

for line in f.readlines():
    split_line = line.split(",")
    pet_type = split_line[0]
    pet_name = split_line[1]
    pet_legs = split_line[2]
    new_pet = Pet(str(pet_type), str(pet_name), int(pet_legs))
    my_pets.append(new_pet)

for pet in my_pets:
    print(pet.type + ":" + pet.name + " has " + str(pet.number_of_legs) + " legs")