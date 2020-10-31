'''
Student name: Luis Zhou
Student ID: 2018100701580033
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
x=int(input("Enter the score:"))
if x>=0 and x<=100:
    if x<50:
        grade='D'
    elif x>50 and x<70:
        grade='C'
    elif x>=70 and x<80:
        grade='B'
    else:
        grade="A"
else:
    print("error")
print('Enter the score:'+str(x))
print('Grade is '+grade)