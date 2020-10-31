#Exercise 14-04
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

f1=open("C:\Temp\my_word.txt","w")
f1.write("The thing the Time Traveller held in his hand was a glittering metallic\nframework, \nscarcely larger than a small clock,\nand very delicately made.")
f1.close()
f2 = open("C:\Temp\my_word.txt", "r")
print(f2.read())