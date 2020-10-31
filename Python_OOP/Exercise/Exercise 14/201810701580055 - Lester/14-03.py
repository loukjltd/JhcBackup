class Pet:
     def __init__(self,type,name,number_legs):
         self.type = type
         self.name = name
         self.number_legs = number_legs

f = open("./pets.txt", "r")
a = []

for line in f.readlines():
    split = line.split(",")
    pet_type = split[0]
    pet_name = split[1]
    pet_legs = split[2]
    new_pet = Pet(pet_type, pet_name, int(pet_legs))
    a.append(new_pet)

for obj in a:
    print(obj.type + obj.name + ":" +str(obj.legs))
