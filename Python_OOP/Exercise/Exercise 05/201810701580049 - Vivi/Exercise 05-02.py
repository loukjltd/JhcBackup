#Exercise 05-02
'''
name:vivi
class:net182
ID：201810701580049
'''

n = int(input("Enter the number of values to insert: "))
myList = []
for i in range(0,n):
    get_num = int(input("Enter a number to insert: "))
    myList.append(get_num)

sum1 = sum(myList)
average = sum(myList)/len(myList)
print(sum1)
print(average)
