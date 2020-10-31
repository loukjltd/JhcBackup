# Exercise 06-04
'''
Student Name: Sean
ID: 201810701580042
Class: Network 182
'''

from tkinter import *
root = Tk()

num1 = 0
num2 = 0
operator = ''


def insertText(num):
    typedNum = num + Entry.get(myEntry)
    myEntry.delete(0, END)
    myEntry.insert(0, typedNum)


def makeOperator(op):
    global num1
    global operator
    num1 = int(Entry.get(myEntry))
    operator = op
    myEntry.delete(0, END)


def calculateAnswer():
    global reset
    num2 = int(Entry.get(myEntry))

    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    elif operator == '*':
        answer = num1 * num2
    elif operator == '/':
        answer = num1 / num2
    myEntry.delete(0, END)
    myEntry.insert(0, str(answer))


topFrame = Frame(root)
topFrame.pack(side=TOP)
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

buttonNum1 = Button(frame2, text='1', width=4, command=lambda: insertText('1'))
buttonNum2 = Button(frame2, text='2', width=4, command=lambda: insertText('2'))
buttonNum3 = Button(frame2, text='3', width=4, command=lambda: insertText('3'))
buttonAdd = Button(frame2, text='+', width=4, command=lambda: makeOperator('+'))
buttonNum1.pack(side=LEFT)
buttonNum2.pack(side=LEFT)
buttonNum3.pack(side=LEFT)
buttonAdd.pack(side=LEFT)

buttonNum4 = Button(frame3, text='4', width=4, command=lambda: insertText('4'))
buttonNum5 = Button(frame3, text='5', width=4, command=lambda: insertText('5'))
buttonNum6 = Button(frame3, text='6', width=4, command=lambda: insertText('6'))
buttonSubtract = Button(frame3, text='-', width=4, command=lambda: makeOperator('-'))
buttonNum4.pack(side=LEFT)
buttonNum5.pack(side=LEFT)
buttonNum6.pack(side=LEFT)
buttonSubtract.pack(side=LEFT)

buttonNum7 = Button(frame4, text='7', width=4, command=lambda: insertText('7'))
buttonNum8 = Button(frame4, text='8', width=4, command=lambda: insertText('8'))
buttonNum9 = Button(frame4, text='9', width=4, command=lambda: insertText('9'))
buttonMultiply = Button(frame4, text='*', width=4, command=lambda: makeOperator('*'))
buttonNum7.pack(side=LEFT)
buttonNum8.pack(side=LEFT)
buttonNum9.pack(side=LEFT)
buttonMultiply.pack(side=LEFT)

buttonNum0 = Button(frame5, text='0', width=4, command=lambda: insertText('0'))
buttonEqual = Button(frame5, text='=', width=9, command=lambda: calculateAnswer())
buttonDivide = Button(frame5, text='/', width=4, command=lambda: makeOperator('/'))
buttonNum0.pack(side=LEFT)
buttonEqual.pack(side=LEFT)
buttonDivide.pack(side=LEFT)

root.mainloop()
