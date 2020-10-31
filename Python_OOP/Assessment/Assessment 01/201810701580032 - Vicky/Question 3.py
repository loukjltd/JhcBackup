#Question 3
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

score = int(input('Enter the score:'))
if score >= 80:
    grade = 'A'
elif score >= 70 and score<80:
    grade = 'B'
elif score >=50 and score<70:
    grade = 'C'
else:
    grade='D'
print("Grade is " + str(grade))
if score >100:
    print('Please enter a score between 0 and 100')
