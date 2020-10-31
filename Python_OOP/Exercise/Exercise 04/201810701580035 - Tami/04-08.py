
# Exercise 04-08
'''
Student Name: Tami
ID: 201810701580035
Class: Network 182
'''
user=input("enter english:")
a=0
for i in user:
    if i in('a','e','i','o','u'):
        print('X',end="")
        a+=1
    else:
        print(i,end="")
print()
print('There are '+str(a)+'vowels in the word or sentence.')

