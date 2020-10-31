# Exercise 06-01
'''
name:Clark
class:net182
I  D:201810701580047
'''
from tkinter import *
root = Tk()
root.title('easy to try')
root.geometry('200x200')
tf = Frame(root)
tf.pack(side=TOP)
bf1 = Frame(root)
bf1.pack()
text = Label(tf, text='don\'t click the OK button', fg='red')
text.pack()
ok = Button(bf1, text='ok', fg='green')
ok.pack(side=LEFT)
cancel = Button(bf1, text='Cancel', fg='blue')
cancel.pack(side=LEFT)
root.mainloop()
