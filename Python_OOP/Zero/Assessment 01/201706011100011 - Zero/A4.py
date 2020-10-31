a=1
while a != "":
    letter = input("Enter a card letter:").lower()
    if letter == "k":
        print("King")
        break
    elif letter == "q":
        print("Queen")
        break
    elif letter == "j":
        print("Jack")
        break
    elif letter == "a":
        print("Ace")
        break
    else:
        print("Try again.")