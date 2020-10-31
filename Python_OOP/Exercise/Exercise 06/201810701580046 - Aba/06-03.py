#exercise 06-03
'''
student name:Aba
class:net182
student id:201810701580046
'''
from tkinter import *
root = Tk()

user_text = Entry(root)
user_text.pack()

label1 = Label(root,text = '')
label1.pack()

def calcC():
    num = float(Entry.get(user_text))
    new_temp = (num - 32)/1.8
    label1.config(text=str(new_temp))
def calcF():
    num = float(Entry.get(user_text))
    new_temp = num*1.8+32
    label1.config(text=str(new_temp))


button1 = Button(root,text = 'celsius',fg='red',command = calcC)
button2 = Button(root,text = 'Fahrenheit',fg='green',command = calcF)
button1.pack(side = LEFT)
button2.pack(side = LEFT)
root.mainloop()
