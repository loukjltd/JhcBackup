#Exercise 02-01
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

meal=44.50
tax=0.0675
tip=0.15
meal=meal+meal*tax
total=meal+meal*tip
print("Total cost of the meal:${0:.2f}".format(meal))
print('')

meal=44.50
tax=0.0675
tip=0.15
meal=meal+meal*tax
meal=meal+meal*tip
pay="Please pay now"
print("Total cost of the meal:${0:.2f}""\n{1}".format(meal,pay))