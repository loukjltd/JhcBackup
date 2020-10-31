# Exercise 04-02
'''
Student Name: shrek
ID: 201810101580038
Class: Network 182
'''

answer = 44
count = 5
while count > 0:
    guess = int(input("Enter a number: "))
    if guess == answer :
        print("You are correct")
        break
    count -= 1
    print("Wrong. Try again. You have " + str(count) + " more tries.")
