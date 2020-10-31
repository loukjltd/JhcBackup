#Exercise 04-10
#Josh net182 201810701580043

num = input('Enter the number for the times table:')
bool1 = False
while bool1 == False:
    try:
        num = int(num)
        for i in range(1,num+1):
            for j in range(1,num+1):
                print(i*j, end='\t')
            print()
        bool1 = True
    except:
        num = input('Please enter a int number:')