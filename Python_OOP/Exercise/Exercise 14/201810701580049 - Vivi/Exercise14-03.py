#Exercise 14-03
"""
class:net182
name:vivi
id:201810701580049
"""
class Pet:
    def __init__(self,type,name,number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs

file = open(r'my_pets.txt',"r")
my_pets = []

for line in file.read().splitlines():
    split_line = line.split(",")
    print(split_line)
    pet_type = str(split_line[0])
    pet_name = str(split_line[1])
    pet_legs = int(split_line[2])

    new_pet = Pet(pet_type,pet_name,pet_legs)
    # print(new_pet)
    my_pets.append(new_pet)

for pet in my_pets:
    print(str(pet.type) + ": "+ str(pet.name) + " has " + str(pet.number_of_legs) + " legs " )
