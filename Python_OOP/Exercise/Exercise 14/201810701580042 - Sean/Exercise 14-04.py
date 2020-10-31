# Exercise 14-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

f1 = open("./my_words.txt", "w")
f1.write("The thing the Time Traveller held in his hand\n"
         "was a glittering metallic\n"
         "framework, \n"
         "scarcely larger than a small clock, \n"
         "and very delicately made.")
f1.close()

f2 = open("./my_words.txt", "r")
print(f2.read())
