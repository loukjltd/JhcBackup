# Qusetion3
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

number=int(input('enter a score: '))
while number>100 or number<0:
    print('Please enter a score between 0 and 100')
    number = int(input('enter a score: '))
    if number<=100 and number>=80:
        print('Grade is A')
    elif number<80 and number>=70:
        print('Grade is B')
    elif number<70 and number>=50:
        print('Grade is C')
    elif number<50 and number>=0:
        print('Grade is D')