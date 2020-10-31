# exercise 05-02
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
user = int(input("Enter the number of values to insert:"))
n = user
Mylist = []

for i in range(0,n):
    get_num = int(input("Enter a number to insert: "))
    Mylist.append(get_num)
sum = sum(Mylist)
average = sum /n
print("Sum is:" , sum)
print("Average is: " , average)