# Exercise 06-01
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

from tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

myLabel = Label(topFrame, text='Do not click the OK button!', fg='red')
myLabel.pack()

buttonOK = Button(bottomFrame, text='OK', fg='green')
buttonCancel = Button(bottomFrame, text='Cancel', fg='blue')
buttonOK.pack(side=LEFT)
buttonCancel.pack(side=RIGHT)

root.mainloop()
