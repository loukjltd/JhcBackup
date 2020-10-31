# exercise 13-01
'''
student name: Eda
ID: 201810701580031
class: network182
'''

def countdown(n):
    if n > 10:
        print("Finished!")
    else:
        print(n)
        countdown(n + 1)
countdown(1)