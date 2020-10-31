'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
score = int(input("Enter the score: "))


if score < 0 or score > 100:
    print("Please enter a score between 0 and 100")
elif score >= 80:
    print("Grade is A")
elif score >= 70:
    print("Grade is B")
elif score >= 50:
    print("Grade is C")
elif score >= 0 and score < 50:
    print("Grade is D")



