'''
student name:Bruce
ID:201810701580057
class: network 182
'''

from tkinter import *
root = Tk()

num1 = 0
num2 = 0

operator = ''

def insertText(num):
    typedNum = myEntry + num
    myEntry.delete(0,END)
    myEntry.insert(0,typedNum)

def makeOperator(op):
    global num1
    global operator
    num1 = int()
    operator = op
