# Exercise 05-02
'''
name:Clark
class:net182
I  D:201810701580047
'''
x = int(input('Enter the number of values to insert: '))
myList = []
for a in range(0, x):
    y = int(input('Enter a number to insert: '))
    myList.append(y)
print('Sum is:', sum(myList))
print('Average is:', sum(myList)/len(myList))
