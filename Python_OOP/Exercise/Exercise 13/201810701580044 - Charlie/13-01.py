'''
student name: Charlie
#ID: 201810701580044
#class: net182
'''
def countdown(n):
    if n > 10:
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
