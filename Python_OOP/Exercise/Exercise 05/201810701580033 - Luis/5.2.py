

# Exercise 05-02
''''
student name:Luis
ID:201810701580033
class:network 182
'''



n=int(input("Enter the number of values to insert: "))
myList=[]

for i in range(0,n):

    get_num=int(input("Enter a number to insert: "))
    myList.append(get_num)

sum =sum(myList)
average=sum/len(myList)
print('Sum is:'+str(sum))
print('Average is:'+str(average))
