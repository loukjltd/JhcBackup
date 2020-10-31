#exercise 05-02
'''
student name: Tami
student id:201810701580035
class:net 182
'''


n = int(input("Enter the number of values to insert: "))
mylist=[]

for a in range(0,n):
    get_num=int(input("Enter a number to insert: "))
    mylist.append(get_num)

sum=(sum(mylist))
average = sum/n
print(str(sum))
print(str(average))
