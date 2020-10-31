'''
Class:Net182
Name:Assass
ID:201810701580040
'''
s = int(input('Enter a score: '))
if s >= 0 or s <= 100:
    if 0 <= s < 50:
        print('Grade is D')
    elif 50 <= s < 70:
        print('Grade is C')
    elif 70 <= s < 80:
        print('Grade is B')
    elif 80 <= s <= 100:
        print('Grade is A')