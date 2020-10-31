#Exercise 05-02
'''
name:leo
idnumber: 201810701580053
class: net182
'''

n=int(input( "Enter the number of values to insert: "))
myList=[]

for a in range(0,n):
    get_num=int(input("Enter a number to insert: "))
    myList.append(get_num)

sum=sum(myList)
average=sum/n
print('sum is '+str(sum))
print('average is '+str(average))
