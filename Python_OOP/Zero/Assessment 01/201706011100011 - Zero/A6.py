import random
rand=random.randint(0,20)

numbers=input("Guess my secret number between 0 and 20 using 4 guesses separated by commas:")
list=[]
a=""
for i in numbers:
    if i!="," :
        a=a+i
    else:
        list.append(a)
        a=""
list.append(a)
#print(list)

d=0
for i in list:
    b=int(i)
    if b==rand:
        d=d+1
if d!=0:
    print("You won! My secret number was:", rand)
else:
    print("You lost! My secret number was:", rand)