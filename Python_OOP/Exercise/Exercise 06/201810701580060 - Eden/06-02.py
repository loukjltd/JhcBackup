'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
from tkinter import * # get everything in tkinter module

import tkinter.messagebox

root = Tk() # make an empty window object

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


myLabel = Label(topFrame,text="    Enter your name:    ",fg="black")
myLabel.pack()

myEntry = Entry(topFrame)
myEntry.pack()

mylistbox1 = Listbox(topFrame)
mylistbox1.insert(0,"Male","Female")
mylistbox1.pack()

def ShowName():
    name = Entry.get(myEntry)
    tkinter.messagebox.showinfo("My name",str(name))

def ChangeName():
    entryEnter.delete(0,END)

button1 = Button(bottomFrame, text="ShowName", fg="red",command = ShowName)
button2 = Button(bottomFrame, text="ChangeName", fg="green")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
root.mainloop()