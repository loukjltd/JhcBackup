# Exercise 14-03
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''


class Pet:

    def __init__(self, type, name, number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs


f = open("./my_pets.txt", "r")
my_pets = []

for line in f.readlines():
    split_line = line.split(",")
    pet_type = split_line[0]
    pet_name = split_line[1]
    pet_legs = split_line[2]
    new_pets = Pet(pet_type, pet_name, int(pet_legs))
    my_pets.append(new_pets)

for obj in my_pets:
    print(str(obj.type) + ': ' + str(obj.name) + ' has ' + str(obj.number_of_legs) + ' legs')
