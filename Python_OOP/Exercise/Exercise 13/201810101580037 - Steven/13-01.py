# exercise13-01
'''
student name: Steven
ID: 201810101580037
class: network 182
'''
def countdown(n):
    if n > 10:
        print("Finished!")
    else:
        print(n)
        countdown(n+1)

countdown(1)
