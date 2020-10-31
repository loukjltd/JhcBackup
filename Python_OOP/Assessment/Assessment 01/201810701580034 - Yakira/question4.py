'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
letter = input("Enter a card letter: ").lower()
while letter != "k" and letter != "q" and letter != "j" and letter != "a":
    print("Try again.")
    letter = input("Enter a card letter: ").lower()
while letter == 'k'or letter == "q" or letter == "j" or letter == "a":
    if letter == "k":
        print('King')
    elif letter == "q":
        print('Queen')
    elif letter == "j":
        print('Jack')
    else:
        print('Ace')
    break