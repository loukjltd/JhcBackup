'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
import random
rand = random.randint(0, 20)
print('Guess my secret number between 0 and 20 using 4 guesses separated by commas:')
sec=str(input('separated by commas: ')).split(',')
num_list=[]
num_list.append(sec)
s=str()
for i in range(0,len(num_list)):
    j=num_list[i]
    i=int(i)
    while i==rand:
        print('You won! My secret number was: '+str(i))
        break
    print('You lost! My secret number was:'+str(rand))