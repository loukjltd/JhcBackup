'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''
num = float(input("Enter the score: "))
if num < 0:
    print("Please enter a score between 0 and 100")
else :
    if num < 50 :
        print("Grade is D")
    else :
        if num < 70 :
            print("Grade is C")
        else :
            if num < 80 :
                print("Grade is B")
            else :
                if num <= 100:
                    print("Grade is A")
                else :
                    print("Please enter a score between 0 and 100")