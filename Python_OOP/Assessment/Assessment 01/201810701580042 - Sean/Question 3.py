# Assessment 1 Question 3
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

score = int(input('Enter a score: '))
if score < 0 or score > 100:
    print('Please enter a score between 0 and 100')
else:
    if 0 <= score < 50:
        print('Grade is D')
    elif 50 <= score < 70:
        print('Grade is C')
    elif 70 <= score < 80:
        print('Grade is B')
    elif 80 <= score <= 100:
        print('Grade is A')
