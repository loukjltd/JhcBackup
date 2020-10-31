dictionary ={"Australia":22.5,"China":36.4,"Malaysia":38.40,"New Zealand":18.2}

list=[]
for key in dictionary:
    list.append(dictionary[key])
    print(key, ':', dictionary[key])

a=0
sum=0
for i in list:
    sum=sum+i
    a+=1
print("Average temperature:",float('%.2f'%(sum/a)))

max=0
for i in list:
    if max<i:
        max=i
print("Average temperature:",float('%.2f'%max))

b=0
for i in list:
    if i>=20 and i<=30:
        b+=1
print("Number of temperatures between 20 and 30:",b)