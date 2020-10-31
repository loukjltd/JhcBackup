a = int(input("Enter a score:"))
if a < 0 or a > 100:
    print("Enter a score again")
else:
    if 0 <= a < 50:
        print("Grade is D")
    elif 50 <= a < 70:
        print("Grade is C")
    elif 70 <= a < 80:
        print("Grade is B")
    elif 80 <= a <= 100:
        print("Grade is A")
