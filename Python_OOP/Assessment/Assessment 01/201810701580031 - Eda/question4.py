#question4
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

b = True
while b:
    a = input("Enter a cars letter: ").lower()
    if a == "k":
        print("King")
        break
    elif a == "q":
        print("Queen")
        break
    elif a == "j":
        print("Jack")
        break
    elif a == "a":
        print("Ace")
        break
    else:
        print("Try again")