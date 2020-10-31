# exercise 06-02
'''
student name:Felix
class:net182
student id:201810701580052
'''
from tkinter import *
import tkinter.messagebox
root = Tk()

topFrame = Frame(root)
topFrame = Label(root,text='Enter you name')
topFrame.pack(side=TOP)
bottomFrame = Frame(root)
bottomFrame.pack()

myName = Entry(topFrame)
myName.pack()
mynameList = Listbox(topFrame)
mynameList.pack()

mynameList.insert(0,'Male')
mynameList.insert(END,'Female')

def showName():
    printname = Entry.get(myName)
    tkinter.messagebox.showinfo('Myname',printname)

def changeName():
    myName.delete(0,END)
    myName.insert(0,'Sam')
    
ShowButton = Button(bottomFrame,text='Show name',fg='red',command=showName)
ChangeButton = Button(bottomFrame,text='Change name',fg='green',command=changeName)
ShowButton.pack(side=LEFT)
ChangeButton.pack(side=LEFT)

root.mainloop()
