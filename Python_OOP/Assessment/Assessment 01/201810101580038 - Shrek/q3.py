#exercise 03
'''
studentname:shrek
student id:201810101580038
class:net182
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