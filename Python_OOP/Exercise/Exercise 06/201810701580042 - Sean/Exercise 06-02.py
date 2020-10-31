# Exercise 06-02
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

from tkinter import *
import tkinter.messagebox

root = Tk()

topFrame = Frame(root)
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

labelEnter = Label(topFrame, text='Enter your name:')
labelEnter.pack()

entryEnter = Entry(topFrame)
entryEnter.pack()
entryEnter.insert(0, 'Enter your name')

userList = Listbox(topFrame)
userList.pack()
userList.insert(0, 'Male')
userList.insert(0, 'Female')


def showName():
    user_text = Entry.get(entryEnter)
    tkinter.messagebox.showinfo('My name', str(user_text))


def changeName():
    entryEnter.delete(0, END)
    entryEnter.insert(0, 'Sam')


showButton = Button(bottomFrame, text='Show name', fg='red', command=showName)
showButton.pack(side=LEFT)
changeName = Button(bottomFrame, text='Change name', fg='green', command=changeName)
changeName.pack(side=RIGHT)

root.mainloop()
