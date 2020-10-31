# exercise 06-02
'''
student name: Eda
ID: 201810701580031
class: network182
'''

from tkinter import *
import tkinter.messagebox as ms
root = Tk()
MyLabel = Label(root,text='Enter your name')
MyLabel.pack()
myEntry = Entry(root)
myEntry.pack()
myEntry.insert(0,'')

def showname():
    name=Entry.get(myEntry)
    print(name)

def changename():
    myEntry.delete(0,END)
    myEntry.insert(0,'Sam')

listbox = Listbox(root)
listbox.insert(END,'Male')
listbox.insert(END,'Female')
listbox.pack()

button1 = Button(root, text = 'show name', fg = 'blue', command = showname)
button2 = Button(root, text = 'change name', fg = 'green', command = changename)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()