'''
class:net182
name:Assass
id:201810710580040
'''
import re as re
class Pet:
    def __init__(self,type,name,number_of_legs):
        self.type=type
        self.name=name
        self.number_of_legs=number_of_legs

f = open("./my_pets.txt", "r")
my_pets=[]

for i in f.readlines():
    split_line=i.split(',')
    pet_type=split_line[0]
    pet_name=split_line[1]
    pet_legs=re.sub('[\n]', '',split_line[2])
    new_pet=Pet(pet_type,pet_name,pet_legs)
    my_pets.append(new_pet)
for i in my_pets:
    print(i.type + ': '+ i.name + ' has ' + i.number_of_legs + ' legs')