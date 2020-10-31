from tkinter import * # get everything in tkinter module
import tkinter.messagebox # import the messagebox class

root = Tk() # make an empty window object

root.title("")
root.geometry("150x200")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)#(side=BOTTOM)

myLabel = Label(topFrame, text="Enter your name")
myLabel.pack()

myEntry=Entry(topFrame)
myEntry.pack()

Listbox1=Listbox(topFrame)
Listbox1.insert(0, "Male")
Listbox1.insert(1, "Female")
Listbox1.pack()

def showName():
    user_text = Entry.get(myEntry)
    tkinter.messagebox.showinfo("My name", user_text)

def changeName():
    myEntry.delete(0, END)
    myEntry.insert(0,"Sam")

button1 = Button(bottomFrame, text="Show name", fg="red",command=showName)
button2 = Button(bottomFrame, text="Change name", fg="green",command=changeName)

button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()  # keep window always open