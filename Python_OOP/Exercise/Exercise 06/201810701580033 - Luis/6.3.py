
# Exercise 06-03
''''
student name:Luis
ID:201810701580033
class:network 182
'''


from tkinter import *
root=Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame=Frame(root)
bottomFrame.pack(side=BOTTOM)

tx1=Entry(topFrame)
tx1.pack()
tx1.insert(0,'')
MyLabel=Label(bottomFrame)
MyLabel.pack()

def calcC():
    c=float(Entry.get(tx1))
    f=c*9/5+32
    MyLabel.config(text=str(f))

def calcF():
    f = float(Entry.get(tx1))
    c=(f-32)*5/9
    MyLabel.config(text=str(c))

Celsius=Button(bottomFrame,text='Celsius',fg='red',command=calcC)
Fahrenheit=Button(bottomFrame,text='Fahrenheit',fg='green',command=calcF)

Celsius.pack(side=LEFT)
Fahrenheit.pack(side=LEFT)

root.mainloop()