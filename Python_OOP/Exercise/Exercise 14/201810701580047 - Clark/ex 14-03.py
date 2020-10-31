class Pet:
    def __init__(self, type, name, number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs


f = open('my_pet.txt', 'r')
my_pets = []

for a in f.readlines():
    split_line = a.split(',')
    pet_type = split_line[0]
    pet_name = split_line[1]
    pet_legs = split_line[2]
    new_pet = Pet(pet_type, pet_name, pet_legs)
    my_pets.append(new_pet)

for b in my_pets:
    print('%s : %s has %d legs' % (b.type, b.name, int(b.number_of_legs)))
