# exercise 04-08
'''
student name: Eda
ID: 201810701580031
class: network182
'''


a = input("Please enter word or sentence:")
b = 0
for i in a:
    if i in ('a','e','i','o','u'):
        print('X',end="")
        b += 1
    else:
        print(i,end="")
print()
print('\d','there are '+ str(a)+'vowels in the word or sentence.')