#Exercise 06-02
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

from tkinter import *
import tkinter.messagebox as ms
root = Tk()
MyLable=Label(root,text='Enter your name')
MyLable.pack()
text1=Entry(root)
text1.pack()
text1.insert(0,'')

def showname():
    name=Entry.get(text1)
    print(name)

def changename():
    text1.delete(0,END)
    text1.insert(0,'Sam')

listbox=Listbox(root)
listbox.insert(END,'Male')
listbox.insert(END,'Female')
listbox.pack()

button1 = Button(root, text = 'show name', fg = 'blue', command = showname)
button2 = Button(root, text = 'change name', fg = 'green', command = changename)

button1.pack(side=LEFT)
button2.pack(side=RIGHT)

root.mainloop()
