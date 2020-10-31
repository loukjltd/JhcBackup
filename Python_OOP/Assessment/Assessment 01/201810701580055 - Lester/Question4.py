b = input("Enter a letter:").lower()

if b != "k" and b != "q" and b !="j" and b !="a":
    print("Try again.")

while 1 == 1:
    if b == "k":
        print("King")
    elif b == "q":
        print("Queen")
    elif b == "j":
        print("Jack")
    elif b == "a":
        print("Ace")
    break
