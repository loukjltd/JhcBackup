#Zero
score = int(input("Enter the score:"))
if score < 0 or score > 100:
    print("Please enter a score between 0 and 100")
elif score >= 0 and score <= 59:
    print("D")
elif score >= 60 and score < 70:
    print("C")
elif score >= 70 and score < 80:
    print("B")
else:
    print("A")