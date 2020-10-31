from tkinter import * # get everything in tkinter module

root = Tk() # make an empty window object

root.title("")
root.geometry("200x50")

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)#(side=BOTTOM)

myEntry=Entry(topFrame)
myEntry.pack()

myLabel = Label(topFrame, text="")
myLabel.pack()

def calcC():
    old_temp = float(Entry.get(myEntry))
    new_temp=32 + old_temp * 1.8
    myLabel.config(text=str(new_temp))

def calcF():
    old_temp = float(Entry.get(myEntry))
    new_temp = (old_temp - 32) / 1.8
    myLabel.config(text=str(new_temp))

button1 = Button(bottomFrame, text="Celsius", fg="red", command=calcC)
button2 = Button(bottomFrame, text="Fahrenheit", fg="green", command=calcF)

button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()  # keep window always open