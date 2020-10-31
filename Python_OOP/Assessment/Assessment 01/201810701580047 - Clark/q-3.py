# Question 3
'''
name:Clark
class:net182
I  D:201810701580047
'''
et = float(input('Enter the score:'))
if 50 >= et > 0:
    print('Grade is D')
elif 70 >= et > 50:
    print('Grade is C')
elif 80 >= et > 70:
    print('Grade is B')
elif 100 >= et > 80:
    print('Grade is A')
else:
    print('Please enter a score between 0 and 100')
