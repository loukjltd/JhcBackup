import random as rdm

i = 0
while i < 3:
    userEnter = str(input('Please enter your number: '))
    pcEnter = str(rdm.randint(0, 2))
    i += 1


def compareAnswers(a, b):
    if userEnter != '0' or userEnter != '1' or userEnter != '2':
        print('Entering Invalid')
    if a == '1' and b == '1':
        print(a + 'vs' + b + 'Balance.')
