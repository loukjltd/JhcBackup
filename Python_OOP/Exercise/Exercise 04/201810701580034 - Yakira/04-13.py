# exercise 04-13
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''
a = True
c = 0
e = 0
while a == True :
    num = int(input("Enter a number: "))
    b = input("Do you want to enter another number?: ")
    c = c + num
    e += 1
    if b == "n" or b == "N":
        a = False

f =float( c / e )

print("Sum = "+ str(c))
print("Average = "+ str(f))
