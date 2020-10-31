#Exercise 05-02
'''
name: Assass
idnumber: 201810701580040
class: network 182
'''
n=int(input("Enter the number of values to insert: "))
myList=[]
for i in range(0,n):
    get_num=int(input("Enter a number to insert: "))
    myList.append(get_num)

sum =sum(myList)
average=sum/n
print(str(sum))
print(str(average))
