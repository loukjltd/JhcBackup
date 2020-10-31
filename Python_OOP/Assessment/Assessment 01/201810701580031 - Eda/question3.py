#question3
'''
student name:Eda xiang
student ID:201810701580031
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

print("Please enter a score between 0 and 100")
a = int(input("Enter the score: "))

if a >= 0 and a < 50:
    print("Grade is  D")
elif a >= 50 and a < 70:
    print("Grade is  C")
elif a >= 70 and a <80:
    print("Grade is  B")
elif a >= 80 and a <=100:
    print("Grade is  A")
else:
    print("error message")