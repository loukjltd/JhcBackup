'''
Student Name: leo
ID: 201810701580053
Class: Network 182
'''
print('Please enter a score between 0 and 100')
score = int(input('Enter the score:'))

if 0 < score <50:
    print("Grade is D")
elif 50 <=  score < 70 :
    print("Grade is C")
elif 70 <=score < 80:
    print("Grade is B")
elif 80 <= score <=100:
    print("Grade is A")