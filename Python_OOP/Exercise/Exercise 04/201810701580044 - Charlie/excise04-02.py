# Exercise 04-02
'''
Student Name: Charlie
ID: 201810101580044
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
