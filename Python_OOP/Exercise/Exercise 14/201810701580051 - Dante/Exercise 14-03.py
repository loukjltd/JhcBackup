# Exercise 014-03
'''
Student Name: dante
ID: 201810701580051
Class: Network 182
'''
class Pet:

    def __init__(self,type,name,number_of_legs):
        self.type=type
        self.name=name
        self.number_of_legs=number_of_legs


f=open('F:\python\my_pets.txt','r')
my_pets=[]

for i in f.readlines():
    split_line=i.split(',')
    pet_type=split_line[0]
    pet_name=split_line[1]
    pet_legs=split_line[2]
    new_pet=Pet(pet_type,pet_name,int(pet_legs))
    my_pets.append(new_pet)

for b in my_pets:
    print(b.type+': '+b.name+' has '+str(b.number_of_legs)+' legs')