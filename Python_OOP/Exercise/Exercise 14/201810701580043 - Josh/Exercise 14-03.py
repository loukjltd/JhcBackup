#Exercise 14-03
#Josh net182 201810701580043

class Pet:
    def __init__(self, type, name, legs):
        self.type = type
        self.name = name
        self.legs = legs

try:
    f = open('./my_pets.txt', 'r')
    my_pets = []
    for i in f.readlines():
        split_line = i.strip('\n').split(',')
        pet_type = split_line[0]
        pet_name = split_line[1]
        pet_legs = split_line[2]
        new_pet = Pet(pet_type, pet_name, pet_legs)
        my_pets.append(new_pet)

    for i in my_pets:
        print(i.type, ':', i.name, 'has', i.legs, 'legs')
finally:
    if f:
        f.close()