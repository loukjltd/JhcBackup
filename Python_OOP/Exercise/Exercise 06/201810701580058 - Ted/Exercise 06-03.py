# Exercise 06-03
'''
Student Name: Ted
ID: 201810701580058
Class: Net 182
'''

from tkinter import *
def celsius():
    calcC=float(Entry.get(label))
    new_temp = (calcC- 32)/1.8
    label2.config(text=str(new_temp))
def Fahrenheit():
    caleF=Entry.get(label)
    new_temp=int(caleF)*1.8+32
    label2.config(text=str(new_temp))
root=Tk()

label=Label(root,text='enter your number !')
label=Entry(root)
label.pack()
label2=Label(root)
label2.pack()

frame=Frame(root)
frame.pack()

bottom1=Button(frame,text='celsius',fg='red',command=celsius)
bottom1.pack(side=LEFT)
bottom2=Button(frame,text='Fahrenheit',fg='green',command=Fahrenheit)
bottom2.pack(side=LEFT)

root.mainloop()
