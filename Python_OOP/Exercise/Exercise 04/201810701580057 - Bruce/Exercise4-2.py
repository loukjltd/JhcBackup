#Exercise4-2
'''
student name:Bruce
ID:201810701580057
class: network 182
'''
answer = 44
count = 5

while count > 0:
    guess = int(input('Enter a number: '))
    if guess == answer:
        print('You are corret')
        break

    count -= 1
    print("Wrong. Try again. You have " + str(count) + " more tries.")
