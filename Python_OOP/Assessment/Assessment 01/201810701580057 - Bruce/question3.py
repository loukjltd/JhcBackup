'''
student name:Bruce
ID:201810701580057
class: network 182
'''

score = int(input('Enter the score: '))

if 0 <= score and score < 50:
    print('Grade is D')
elif 50 <= score and score < 70:
    print('Grade is C')
elif 70 <= score and score < 80:
    print('Grade is B')
elif 80 <= score and score <= 100:
    print('Grade is A')
else:
    print('Please enter a score between 0 and 100')