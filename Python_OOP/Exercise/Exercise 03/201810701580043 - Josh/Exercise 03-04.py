#Exercise 03-04
#Josh net182 201810701580043

age = int(input("Enter your age: "))
if age<2:
    print("You are a baby.")
else:
    if age<13:
        print("You are a child.")
    else:
        if age<20:
            print("You are a teenager..")
        else:
            print("You are an adult.")