# exercise 14-04
'''
student name: Yakira
ID: 201810701580034
class: network182
'''
f1 = open("D:\drive\my_words.txt", "w")
f1.write("The thing the Time Traveller held in his hand\n"
         "was a glittering metallic\nframework,\n"
         "scarcely larger than a small clock,\n"
         "and very delicately made.")
f1.close()

f2 = open("D:/drive/my_words.txt", "r")
print(f2.read())
