#Exercise 13-01
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

def countdown(n):

    if n >10 :
        print("Finished")
    else:
        print(n)
        countdown(n+1)

countdown(1)