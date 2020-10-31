#exercise 06-02
'''
student name:dante
class:net182
student id:201810701580051
'''

from tkinter import *
import tkinter.messagebox

root = Tk()

def showname():
    name = Entry.get(user_text)
    tkinter.messagebox.showinfo("My name", name)
def changename():
    tkinter.messagebox.showinfo('Sam')

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

label1 = Label(topFrame,text = 'Enter your name:')
label1.pack()

user_text = Entry(topFrame)
user_text.pack()
listbox=Listbox(topFrame)
listbox.insert(0,'Male')
listbox.insert(END,'Female')
listbox.pack()

button1 = Button(bottomFrame,text = 'Show name',fg='red',command = showname)
button2 = Button(bottomFrame,text = 'Change name',fg='green',command = changename)
button1.pack(side = LEFT)
button2.pack(side = LEFT)
root.mainloop()