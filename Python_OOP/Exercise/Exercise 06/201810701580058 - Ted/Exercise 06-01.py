# Exercise 06-01
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

from tkinter import *

root = Tk()
root.title('tk')
root.geometry('240x90')

topFrame = Frame(root)
topFrame.pack()

myLabel = Label(topFrame, text="Do not click the OK button!",fg='red')
myLabel.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="OK", fg="green")
button2 = Button(bottomFrame, text="Cancel", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)


root.mainloop()
