#Exercise 05-02
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

n=int(input("Enter the number of values to insert: "))
mylist=[]

for a in range(0,n):
    get_num=int(input("Enter a number to insert: "))
    mylist.append(get_num)

sum=sum(mylist)
average=sum/len(mylist)
print('sum is '+str(sum))
print('average is '+str(average))