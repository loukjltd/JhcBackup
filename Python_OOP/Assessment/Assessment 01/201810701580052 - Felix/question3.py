score = int(input('Enter the score: '))


if score<0 or score>100:
    print('Please enter a score between 0 and 100')
elif score>=80 and score<=100:
    print("grade = A")
elif score>=70 and score<80:
    print("grade = B")
elif score>=60 and score<70:
    print("grade = C")
else :
    print("grade = D")


