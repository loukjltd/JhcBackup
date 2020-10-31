'''
Class:Net182
Name:Lester
ID:201810701580055
'''

n = int(input("Enter the number of values to insert: "))
myList = []
for a in range (0,n):
    get_num = int(input("Enter a number to insert: "))
    myList.append(get_num)

sum=sum(myList)
average=sum/n
print(sum)
print(average)
