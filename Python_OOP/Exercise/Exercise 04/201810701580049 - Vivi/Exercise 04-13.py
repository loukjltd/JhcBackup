#Exercise 04-13
'''
class:net182
name:vivi
id:201810701580049
'''
bool1 = False
sum, count = 0, 0
while bool1 == False:
    try:
        num = float(input('Enter a number:'))
        sum += num
        count += 1
        bool2 = False
        while bool2 == False:
            yon = input('Do you want to enter another number?:')
            if yon == 'Y' or yon == 'y':
                bool2 = True
            elif yon == 'N' or yon == 'n':
                bool1, bool2 = True, True
                print('Sum = '+str(sum))
                print('Average = '+str(sum/count))
            else:
                print('Please enter \'Y/y\' or \'N/n\'!')
    except:
        print('Please enter a number!')
