from tkinter import *
root = Tk()
root.title("")
root.geometry("160x90")
topFrame = Frame(root)
topFrame.pack()

topFrame = Frame(root)
topFrame.pack(side=TOP)
myEntry = Entry(topFrame)
myEntry.pack()
myLabel = Label(topFrame, text="")
myLabel.pack()

def calcC():
    old_temp = float(Entry.get(myEntry))
    new_temp = 32 + old_temp * 1.8
    myLabel.config(text=str('%.1f %s' % (new_temp, "Fahrenheit")))
def calcF():
    old_temp = float(Entry.get(myEntry))
    new_temp = (old_temp - 32) / 1.8
    myLabel.config(text=str('%.2f %s' % (new_temp, "Celsius")))

button1 = Button(topFrame, text="Celsius", fg="red", command=calcC)
button2 = Button(topFrame, text="Fahrenheit", fg="blue", command=calcF)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

root.mainloop()