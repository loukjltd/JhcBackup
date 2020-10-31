#Question 5
#Josh net182 201810701580043

str1 = input('Enter a list of numbers separated by commas:')
try:
    f = open('./some_numbers.txt', 'w')
    f.write(str1)
    f.close()
    f = open('./some_numbers.txt', 'r')
    line_of_numbers = f.readline()
    numlist = line_of_numbers.split(',')
    numlist1 = []
    for i in numlist:
        print(i)
        numlist1.append(int(i))
    print('Sum: {0}'.format(sum(numlist1)))
    print('Maximum: {0}'.format(max(numlist1)))
except IOError:
    print('Not found')
finally:
    if f:
        f.close()