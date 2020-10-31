#Question 3
"""
class:net182
name:vivi
id:201810701580049
"""
user_input = int(input("Enter a number: "))
def fact(user_input):
    if user_input == 0:
        return 1
    else:
        return (user_input % 10) * fact(int(user_input / 10))
print("The product of all of the digits of {} is {}".format(user_input,fact(user_input)))
exit(0)
