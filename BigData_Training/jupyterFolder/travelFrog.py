# Define class, frog
class travelFrog:
    # Define method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Eat something
    def eat(self):
        print(self.name, 'is having dinner.')

    # Moving
    def move(self):
        print(self.name, 'is jumping.')

    # How old are you?
    def oldAge(self):
        print(self.name, 'is', self.age, 'years old.')


frog1 = travelFrog('Mr.White', '20')

frog1.eat()
frog1.move()
frog1.oldAge()
print('\n')

frog2 = travelFrog('Mr.Zhang', '38')

frog2.eat()
frog2.move()
frog2.oldAge()
