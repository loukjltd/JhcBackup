print("Enter the first line of numbers separated by commas:")
list1=input()
print("Enter the second line of numbers separated by commas:")
list2=input()

list_1=[]
a=""
for i in list1:
    if i!="," :
        a=a+i
    else:
        list_1.append(a)
        a=""
list_1.append(a)
print(list_1)

list_2=[]
b=""
for i in list2:
    if i!="," :
        b=b+i
    else:
        list_2.append(b)
        b=""
list_2.append(b)
print(list_2)

c=0
for i in list_1:
    for j in list_2:
        if i==j:
            c+=1
print(c)