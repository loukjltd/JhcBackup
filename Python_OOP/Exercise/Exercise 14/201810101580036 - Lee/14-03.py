'''
class:net182
name:Lee
ID:201810101580036
'''
class Pet:
    def __init__(self,type,name,number_of_legs):
        self.type = type
        self.name = name
        self.number_of_legs = number_of_legs

f = open('D:\my_pets.txt','r')
my_pets = []

for line in f.readlines():
    split_line = x.split(',')
    pet_type = split_line[0]
    pet_name = split_line[1]
    pet_legs = split_line[2]
    new_pets = Pet(pet_name,int(pet_legs),pet_type)
    my_pets.append(new_pet)
for obj in my_pets:
    print(str(obj.type) + ':' + str(obj.name) + 'has' + str(obj.number_of_legs) + 'legs')