# exercise 14-04
'''
student name: Eda
ID: 201810701580031
class: network182
'''
f1=open("./my_word.txt","w")
f1.write("The thing the Time Traveller held in his hand \nwas a glittering metallic\nframework, \nscarcely larger than a small clock,\nand very delicately made.")
f1.close()
f2 = open("./my_word.txt", "r")
print(f2.read())