'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
a=str(input('Enter the first line of numbers separated by commas: ')).split(',')
b=str(input('Enter the second line of numbers separated by commas: ')).split(',')

n1_list=[]
n1_list.append(a)
n2_list=[]
n2_list.append(b)
s=0
for i in n1_list:
    for k in n2_list:
       while i==k:
           s=s+1
           break
print("There are "+str(s)+ " numbers that are in both lists")