#Question 3
#Josh net182 201810701580043

sco = int(input('Enter the score: '))
if sco >= 0 and sco < 50:
    print('Grade is D')
elif sco >= 50 and sco < 70:
    print('Grade is C')
elif sco >= 70 and sco < 80:
    print('Grade is B')
elif sco >= 80 and sco <= 100:
    print('Grade is A')
else:
    print('Grade error')