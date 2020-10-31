'''name;Faker
   ID number:201810701580048
   class:net 182'''
age = int(input("Enter your age:"))
if age < 0:
    print("You are not man")
else :
    if age < 2 :
        print("You are a baby")
    else :
        if age < 13 :
           print("You are a child")
        else :
            if age < 20 :
               print("You are a teenager")
            else :
               print("You are an adult")
