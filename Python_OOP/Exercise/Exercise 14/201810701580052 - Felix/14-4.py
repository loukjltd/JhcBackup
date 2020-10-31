# Exercise 14-04
'''
student name: felix
#ID: 201810701580052
#class: net182
'''
f1 = open(".\my_words.txt", "w")
f1.write("The thing the Time Traveller held in his hand was a glittering metallic"
         "\nframework,"
         "\nscarcely larger than a small clock,"
         "\nand very delicately made.")
f1.close()

f2 = open(".\my_words.txt", "r")
print(f2.read())
