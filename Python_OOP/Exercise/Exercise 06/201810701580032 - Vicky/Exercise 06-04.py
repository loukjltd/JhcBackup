#Exercise 06-04
'''
student name :Vicky
ID:201810701580032
class:Net182
'''

from tkinter import *
root = Tk()

num1=0
num2=0
operator=''

topFrame = Frame(root)
topFrame.pack()
frame1 = Frame(root)
frame1.pack()
frame2 = Frame(root)
frame2.pack()
frame3 = Frame(root)
frame3.pack()
frame4 = Frame(root)
frame4.pack()
frame5 = Frame(root)
frame5.pack(side=BOTTOM)

myEntry = Entry(frame1, justify=RIGHT)
myEntry.pack()

def insertText(num):
    myEntry.insert(END, num)

def makeOperator(op):
    global num1
    global operator
    num1 = Entry.get(myEntry)
    operator = op
    myEntry.delete(0, END)


def calculateAnswer():
    global reset
    num2 = int(Entry.get(myEntry))
    if operator == "+":
        answer = int(num1) + int(num2)
    elif operator == "*":
        answer = int(num1) * int(num2)
    elif operator == "-":
        answer = int(num1) - int(num2)
    elif operator == "/":
        answer = int(num1) / int(num2)
    myEntry.delete(0, END)
    myEntry.insert(0,END)

button1 = Button(frame2, text="1", command=lambda: insertText('1'))
button2 = Button(frame2, text="2", command=lambda: insertText('2'))
button3 = Button(frame2, text="3", command=lambda: insertText('3'))
buttonPlus = Button(frame2, text="+", command=lambda: makeOperator('+'))

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
buttonPlus.pack(side=LEFT)

button4 = Button(frame3, text="4", command=lambda: insertText('4'))
button5 = Button(frame3, text="5", command=lambda: insertText('5'))
button6 = Button(frame3, text="6", command=lambda: insertText('6'))
buttonPlus1 = Button(frame3, text="-", command=lambda: makeOperator('-'))

button7 = Button(frame4, text="7", command=lambda: insertText('7'))
button8 = Button(frame4, text="8", command=lambda: insertText('8'))
button9 = Button(frame4, text="9", command=lambda: insertText('9'))
buttonPlus2 = Button(frame4, text="*", command=lambda: makeOperator('*'))

button0 = Button(frame5, text="0", command=lambda: insertText('0'))
buttonEquals = Button(frame5, text="=", width=4, command=lambda: calculateAnswer())
buttonDivide = Button(frame5, text="/", command=lambda: makeOperator('/'))

button0.pack(side=LEFT)
buttonEquals.pack(side=LEFT)
buttonDivide.pack(side=LEFT)

root.mainloop()