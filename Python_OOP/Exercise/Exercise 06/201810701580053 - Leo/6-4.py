'''
name:leo
id:201810701580053
class:net182
'''
from tkinter import *

root = Tk()

num1 =0
num2 = 0
Operator = ''



def insertText(num):
   typedNum = num+myEntry.get()
   myEntry.delete(0, END)  # Delete the value in the text box
   myEntry.insert(0, typedNum)  # Put the new value in the text box



def makeOperator(op):
    global num1
    global operator
    num1 = int(myEntry.get())
    operator= op
    myEntry.delete(0, END)

def calculateAnswer():
    global reset  # We need to use the global variable
    num2 = int(myEntry.get())

    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
          answer = num1 + num2

    elif operator == "*":
        answer = num1 + num2
    elif operator == "/":
            answer = num1 + num2

    myEntry.delete(0, END)
    myEntry.insert(0,str(answer))
    
# Make the frames
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

# Make the text box
myEntry = Entry(frame1, justify=RIGHT)
myEntry.pack()
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
buttonPlus = Button(frame3, text="-", command=lambda: makeOperator('-'))

button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)
buttonPlus.pack(side=LEFT)

button7 = Button(frame4, text="7", command=lambda: insertText('7'))
button8 = Button(frame4, text="8", command=lambda: insertText('8'))
button9 = Button(frame4, text="9", command=lambda: insertText('9'))
buttonPlus = Button(frame4, text="*", command=lambda: makeOperator('*'))

button7.pack(side=LEFT)
button8.pack(side=LEFT)
button9.pack(side=LEFT)
buttonPlus.pack(side=LEFT)




button0 = Button(frame5, text="0", command=lambda: insertText('0'))
buttonEquals = Button(frame5, text="=", width=4, command=lambda: calculateAnswer())
buttonDivide = Button(frame5, text="/", command=lambda: makeOperator('/'))

button0.pack(side=LEFT)
buttonEquals.pack(side=LEFT)
buttonDivide.pack(side=LEFT)

root.mainloop()

