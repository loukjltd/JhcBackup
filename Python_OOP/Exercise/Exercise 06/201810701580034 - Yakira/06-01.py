# exercise 06-01
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''

from tkinter import *

root = Tk()
myLabel = Label(root, text="Do not click the OK button", fg="red")
myLabel.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="OK", fg="green")
button2 = Button(bottomFrame, text="Cancel", fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()
