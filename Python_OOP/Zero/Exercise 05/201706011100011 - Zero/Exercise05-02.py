#net171 wuzhengbo
n=int(input("Enter the number of values to insert:"))
myList=[]
sum=0
for i in range(n):
    get_num=int(input("Enter a number to insert:"))
    myList.append(get_num)
    sum+=get_num
average=sum/n
print("Sum is:",sum)
print("Average is:",average)