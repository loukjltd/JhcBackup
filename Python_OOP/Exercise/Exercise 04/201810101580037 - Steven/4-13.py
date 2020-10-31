# exercise04-13
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
k=1
n=int(input("Enter a number:"))
y=input("Do you want to enter another number?:")
s = n
while y == "y" or y== "Y":
    n = int(input("Enter a number:"))
    y = input("Do you want to enter another number?:")
    s=s+n
    k=k+1
if y == "n" or y == "N":
    print("Sum = "+ str(s))
    print("Average = "+str(s/k))
