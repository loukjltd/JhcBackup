# exercise 06-02
'''
student name : Yakira
ID : 201810701580034
class : Net182
'''

from tkinter import *
import tkinter.messagebox as ms

window = Tk()
window.title('tk')
window.geometry('200x400')

myLabel = Label(window, text="Enter your name:")
myLabel.pack()

topFrame = Frame(window)
topFrame.pack()

bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)

tx = Entry(window)
tx.pack()
tx.insert(0,'')

lb = Listbox(window)
lb.pack()
lb.insert(0, 'Male')
lb.insert(END, "Female")
def showName():
    name = Entry.get(tx)
    ms.showinfo('My name', name)
def changeName():
    ms.showinfo('My name', 'Sam')


bottomFrame.pack(side=BOTTOM)

button1 = Button(bottomFrame, text="Show name", fg="red", command=showName)
button2 = Button(bottomFrame, text="Change name", fg="green", command=changeName)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
window.mainloop()
