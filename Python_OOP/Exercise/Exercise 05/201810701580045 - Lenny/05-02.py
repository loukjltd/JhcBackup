#exercise 05-02
'''
name:Lenny
class:net182
ID:201810701580045
'''
n = int(input('Enter the number of values to insert:'))
mylist =[]
for i in range(0,n):
    get_num = int(input('Enter a number to insert:'))
    mylist.append(get_num)

sum = sum(mylist)
average = sum/n

print(sum)
print(average)
