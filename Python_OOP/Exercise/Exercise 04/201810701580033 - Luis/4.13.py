# Exercise 04-13
''''
student name:Luis
ID:201810701580033
class:network 182
'''

a =True
c=0
s=0
while a == True :
    num = int(input("Enter a number: "))
    b = input("Do you want to enter another number?: ")
    s = c + num
    c += 1
    if b == "n" or b == "N":
        a = False

print("Sum = "+ str(c))
print("Average = "+ str(float(s/c)))
