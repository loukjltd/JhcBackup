#Task3
"""
id : 201810701580049
class : Net182
name : vivi
"""

score = int(input("Enter the score: "))
if 0 <= score < 50:
    print("Grade is D")
elif 50 <= score < 70:
    print("Grade is C")
elif 70 <= score < 80:
    print("Grade is B")
elif 80 <= score <= 100:
    print("Grade is A")
else:
    print("Please enter a score between 0 and 100")