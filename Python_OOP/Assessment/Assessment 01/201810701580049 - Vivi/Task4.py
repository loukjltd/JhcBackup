#Task4
"""
id : 201810701580049
class : Net182
name : vivi
"""
dirct = {"K":"King" , "Q":"Queen" , "J":"Jack", "A":"Ace"}
bool = True
while bool == True:
    user_input = input("Please enter a card letter: ")
    key = user_input.upper()
    for i in dirct:
        if key == i:
            print(dirct[i])
            bool = False
            break
    if bool != False:
        print("try again")


