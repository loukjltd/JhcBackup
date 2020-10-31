# exercise 05 02
'''
Bro
201810701580056
network 182
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