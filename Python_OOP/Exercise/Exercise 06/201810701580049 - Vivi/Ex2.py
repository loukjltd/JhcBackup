#Exercise 06-02
'''
class net182
id 2018100701580049
name vivi
'''

from tkinter import *
import tkinter.messagebox


def showName():
    tkinter.messagebox.showinfo("My name", Entry.get(text))


def ChangeName():
    w = Entry.get(text)
    name_list.insert(0, w)
    tkinter.messagebox.showinfo("My name", w)


root = Tk()

topFrame = Frame(root)
topFrame.pack()
myLabel = Label(topFrame, text="Enter your name:") #
myLabel.pack() # put the text in the window

text = Entry(topFrame,state="normal")
text.pack()

name_list = Listbox(topFrame)
name_list.insert(0,"male")
name_list.insert(1,"Female")
name_list.pack()


button1 = Button(topFrame, text="Show name", fg = "red" , command=showName)
button2 = Button(topFrame, text="Change name", fg="green" , command=ChangeName)
# make the buttons show
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop() # keep window always open
