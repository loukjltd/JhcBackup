#Exercise 06-02
#Josh net182 201810701580043

from tkinter import *
import tkinter.messagebox as box
# make up the window
root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
# functions
def showName():
    name = en1.get()
    box.showinfo('My name',name)

def changeName():
    en1.delete(0,END)
    en1.insert(0, 'Sam')
    box.showinfo('My name',en1.get())

# main
lab1 = Label(topFrame, text='Enter your name:')
lab1.pack()

en1 = Entry(topFrame)
en1.pack()

lis1 = Listbox(topFrame)
lis1.pack()
lis1.insert(END, 'Male')
lis1.insert(END, 'Female')

butt1 = Button(bottomFrame, text = 'Show name', command = showName, fg = 'red')
butt1.pack(side=LEFT)

butt2 = Button(bottomFrame, text = 'Change name', command = changeName, fg = 'green')
butt2.pack(side=LEFT)
root.mainloop()