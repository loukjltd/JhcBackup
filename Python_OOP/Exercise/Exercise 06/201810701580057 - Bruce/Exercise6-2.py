'''
student name:Bruce
ID:201810701580057
class: network 182
'''

from tkinter import *
import tkinter.messagebox

root = Tk()

def showName():
    name = Entry.get(user_text)
    tkinter.messagebox.showinfo('My name',name)

def changename():
    tkinter.messagebox.showinfo('Sam')

topFrame = Frame(root)
topFrame.pack()

label = Label(topFrame, text='Enter your name: ')
label.pack()

user_text = Entry(topFrame)
user_text.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

listbox = Listbox(topFrame)
listbox.insert(0,'Male')
listbox.insert(END,'Female')
listbox.pack()

button1 = Button(bottomFrame, text='Show name', fg='red',command=showName)
button2 = Button(bottomFrame, text='Change name', fg='green', command=changename)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()