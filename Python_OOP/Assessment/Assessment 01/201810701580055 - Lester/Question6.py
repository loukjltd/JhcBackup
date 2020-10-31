import random
rand = random.randint(0, 20)
list = []
print("Guess my secret number between 0 and 20 using 4 guesses")
a = input("separated by commas")

for i in a.split(""):
    list.append(int(i))

if rand in list:
    print("You won! My secret number was:" + str(rand))
else:
    print("You lost! My secret number was:" + str(rand))
