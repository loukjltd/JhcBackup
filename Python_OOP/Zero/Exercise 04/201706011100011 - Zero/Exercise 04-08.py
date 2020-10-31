#net171 Zero

studentNum=int(input("Enter the number of student grades:"))
for i in range(0,studentNum):
    #print("Enter grade",i+1,":")
    grade=int(input("Enter grade "+str(i+1)+":"))
    if grade>=50:
        print("Student has passed ")
    else:
        print("Student has failed")