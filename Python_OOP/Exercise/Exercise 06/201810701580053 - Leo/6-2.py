'''
name:leo
id:201810701580053
class:net182
'''
from tkinter import * # get everything in tkinter module
import tkinter.messagebox # import the messagebox class

root = Tk() # make an empty window object


topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

label1 = Label(topFrame, text="Enter your name:")
label1.pack()
entry1 = Entry(topFrame)
entry1.pack()
listbox1 = Listbox(topFrame)
listbox1.pack()
listbox1.insert(0, 'Male')
listbox1.insert(END, 'Female')

def showName():
    entry2 = Entry.get(entry1)
    tkinter.messagebox.showinfo("my name", entry2)
def changename():
    entry1.delete(0, END)
    entry1.insert(0, 'Sam')
button1 = Button(bottomFrame, text="Show name ", fg="red",command = showName)
button2 = Button(bottomFrame, text="Change name", fg="green",command = changename)

button1.pack(side=LEFT)
button2.pack(side=LEFT)
root.mainloop()
