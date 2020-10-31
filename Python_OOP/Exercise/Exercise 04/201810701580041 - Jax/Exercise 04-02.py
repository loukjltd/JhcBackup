#Exercise 04-02
'''
name: Jax
idnumber: 201810701580041
class: net182
'''

answer=44
count=5
while count>0:
    message=int(input("Enter a number: "))
    if message==answer:
        print("You are correct")
        break
    count-=1
    print("Wrong. Try again. You have " + str(count) + " more tries.")
