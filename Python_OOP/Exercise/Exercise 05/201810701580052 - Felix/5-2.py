# Exercise 05-02
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
n = int(input ("Enter the number of values to insert: "))
myList = []
count = 0
for i in range(0,n):
    get_num=int(input("Enter a number to insert: "))
    count +=1
    myList.append(get_num)

sum = sum(myList)
average = sum/count
print(sum)
print(average)
