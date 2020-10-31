#Zero
num = int(input("How many sensors are currently collecting data?:"))
temp=[]
for i in range(num):
    q=float(input("Enter temperature "+str((i+1))+":"))
    temp.append(q)

sum=0
for i in temp:
    sum=sum+i
avg=sum/num
print("Average temperature:",float('%.2f'%avg))

max=temp[0]
for i in range(1,num):
    if max>temp[i]:
        max=max
    else:
        max=temp[i]
print("Maximum temperature:",max)

b=0
for i in temp:
    if i>=10 and i<=20:
        b=b+1
print("Number of temperatures between 10 and 20:",b)