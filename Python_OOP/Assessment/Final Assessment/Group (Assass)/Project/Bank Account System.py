from tkinter import *
from Bank import *                                  # 用于调用Bank的class类中的方法

root = Tk()
root.title('Bank Account System')
root.geometry('950x650')
root.resizable(0, 0)


# 框架一、二输出框及菜单栏函数
number = 0
string_account_id = ''
amount = ''
Bank_Account_Tasks().read_data()                    # 读取data.txt的文本内容


def menu_text():                                    # 菜单
    export.delete(0.0, END)
    export.insert(INSERT, '*****************************\n*     '
                          'Bank Account Menu     *\n*****************************\n')
    export.insert(END, '\n1.Menu\n2.Put money in\n3.Get money out\n4.Show account with most money\n')
    export.insert(END, '5.Show account with most transactions\n6.Show one account\n7.Show all account')
    export.insert(END, '\n8.Show total number of transactions\n9.Exit')


def act_put_money():                                # 存钱
    global number
    number = 1
    export.delete(0.0, END)
    export.insert(INSERT, 'put money in...\nEnter the account ID:\n')


def act_get_money():                                # 取钱
    global number
    number = 2
    export.delete(0.0, END)
    export.insert(INSERT, 'get money out...\nEnter the account ID:\n')


def act_most_money():                               # 看最多钱
    export.delete(0.0, END)
    export.insert(INSERT, 'Account with most money:\n')
    export.insert(END, Bank_Account_Tasks().show_biggest_account())             # 在文本框输出调用方法


def act_most_deal():                                # 最多次交易的账户
    export.delete(0.0, END)
    export.insert(INSERT, 'Account with most transactions:\n')
    export.insert(END, Bank_Account_Tasks().most_transactions())                # 在文本框输出调用方法


def act_one_account():                              # 查看一个账户
    global number
    number = 3
    export.delete(0.0, END)
    export.insert(INSERT, 'Show one account...\nEnter the account ID:\n')


def act_all_account():                              # 查看所有账户
    export.delete(0.0, END)
    export.insert(INSERT, 'Showing all accounts...\n\n')
    export.insert(END, Bank_Account_Tasks().all_account())                      # 在文本框输出调用方法


def act_all_transaction():                          # 查看所有交易
    export.delete(0.0, END)
    export.insert(INSERT, 'Total transactions:\n')
    export.insert(END, Bank_Account_Tasks().get_number_of_transactions())       # 在文本框输出调用方法


def shut_down():
    Bank_Account_Tasks().clear()                                                # 清除交易次数并退出
    root.quit()

# 框架三输入相关函数


def act_insert(num):                                # 在输入框输入数字
    my_entry.insert(END, num)


def act_clear():                                    # 清除输入框的内容
    my_entry.delete(0, END)


def act_enter():
    global number, amount, string_account_id                # 调用外部变量
    if not string_account_id.isdigit():                 # 判断参数是否为数字
        string_account_id = my_entry.get()              # 获取输入框的内容
        export.insert(END, string_account_id)           # 文本框输出参数string_account_id
        my_entry.delete(0, END)                         # 删除输入框内容
        if number == 1 or number == 2:                  # 判断是执行存钱、取钱还是查看账户
            export.insert(END, '\nEnter amount:\n')
    if Bank_Account_Tasks().check_account(string_account_id):       # 判断在data.txt中是否存在
        if number == 1:
            if my_entry.get().isdigit():
                amount = float(my_entry.get())          # 将变量转换为浮点数
                export.insert(END, '%.0f\n' % amount)   # 在文本框输出amount不保留小数点
                export.insert(END, Bank_Account_Tasks().put_money_in(string_account_id, amount))   # 在文本框输出调用方法
                string_account_id = ''
                amount = ''                     # 这三个由于重置变量
                number = 0
                my_entry.delete(0, END)
        elif number == 2:                       # 同理number == 1
            if my_entry.get().isdigit():
                amount = float(my_entry.get())
                export.insert(END, '%.0f\n' % amount)
                export.insert(END, Bank_Account_Tasks().get_money_out(string_account_id, amount))  # 在文本框输出调用方法
                string_account_id = ''
                amount = ''
                number = 0
                my_entry.delete(0, END)
        elif number == 3:
            export.insert(END, '\n%s' % Bank_Account_Tasks().show_account(string_account_id))      # 在文本框输出调用方法
            string_account_id = ''
            number = 0
            my_entry.delete(0, END)
    else:                                               # data.txt不存在则输出以下内容
        string_account_id = ''
        export.insert(END, '\nPlease enter exist account:\n')


# 框架四函数
def remove():
    Bank_Account_Tasks().delete_account(account_list.get(ACTIVE))   # 在文档中删除列表选中项
    account_list.delete(ACTIVE)                                     # 在列表中删除列表选中项


# 框架
frame1 = Frame(root)
frame1.place(y=10, width=950, height=250)
frame2 = Frame(root, width=300, height=400)
frame2.place(y=250, x=0)
frame3 = Frame(root, width=350, height=400)
frame3.place(y=250, x=300)
frame4 = Frame(root, width=300, height=400)
frame4.place(y=250, x=650)
# 框架一控件
export_scroll = Scrollbar(frame1)                                   # 滚动条
export_scroll.place(x=750, width=20, height=225)
export = Text(frame1)                                               # 文本框
export.place(x=150, width=600, height=225)
export.config(yscrollcommand=export_scroll.set)                     # 关联滑动条
export_scroll.config(command=export.yview)                          # 拖动文本框时更新文本框内容


# 框架二控件
menu = Button(frame2, text='Menu', command=menu_text).place(x=40, y=10, width=220, height=40)            # 菜单
put_money = Button(frame2, text='Put money in', command=act_put_money).place(x=40, y=50, width=220, height=40)  # 存钱
get_money = Button(frame2, text='Get money out', command=act_get_money).place(x=40, y=90, width=220, height=40)  # 取钱
show_most = Button(frame2, text='Show account with most money', command=act_most_money)                      # 看最多钱
show_most.place(x=40, y=130, width=220, height=40)
show_transactions = Button(frame2, text='Show account with most transactions', command=act_most_deal)        # 最多操作
show_transactions.place(x=40, y=170, width=220, height=40)
show_one = Button(frame2, text='Show one account', command=act_one_account)                                  # 看一个账户
show_one.place(x=40, y=210, width=220, height=40)
show_all = Button(frame2, text='Show all account', command=act_all_account)                                  # 看所有账户
show_all.place(x=40, y=250, width=220, height=40)
show_total = Button(frame2, text='Show total number of transactions', command=act_all_transaction)       # 处理多少次账务
show_total.place(x=40, y=290, width=220, height=40)
end = Button(frame2, text='Exit', command=shut_down).place(x=40, y=330, width=220, height=40)                     # 退出
# 框架三控件
my_entry = Entry(frame3, justify=RIGHT)                                                                   # 输入账户
my_entry.place(x=15, y=20, width=320, height=20)
# lambda是匿名函数
num1 = Button(frame3, text='1', command=lambda: act_insert('1')).place(x=25, y=45, width=100, height=80)           # 1
num2 = Button(frame3, text='2', command=lambda: act_insert('2')).place(x=125, y=45, width=100, height=80)          # 2
num3 = Button(frame3, text='3', command=lambda: act_insert('3')).place(x=225, y=45, width=100, height=80)          # 3
num4 = Button(frame3, text='4', command=lambda: act_insert('4')).place(x=25, y=125, width=100, height=80)          # 4
num5 = Button(frame3, text='5', command=lambda: act_insert('5')).place(x=125, y=125, width=100, height=80)         # 5
num6 = Button(frame3, text='6', command=lambda: act_insert('6')).place(x=225, y=125, width=100, height=80)         # 6
num7 = Button(frame3, text='7', command=lambda: act_insert('7')).place(x=25, y=205, width=100, height=80)          # 7
num8 = Button(frame3, text='8', command=lambda: act_insert('8')).place(x=125, y=205, width=100, height=80)         # 8
num9 = Button(frame3, text='9', command=lambda: act_insert('9')).place(x=225, y=205, width=100, height=80)         # 9
num0 = Button(frame3, text='0', command=lambda: act_insert('0')).place(x=125, y=285, width=100, height=80)         # 0
clear = Button(frame3, text='C', command=act_clear).place(x=25, y=285, width=100, height=80)                       # C
enter = Button(frame3, text='ENTER', command=act_enter)                                                        # ENTER
enter.place(x=225, y=285, width=100, height=80)
# 框架四控件
title = Label(frame4, text='Accounts:').place(width=300, height=20)         # label框
account_list = Listbox(frame4)                                              # 列表框
account_list.place(x=75, y=20, width=150, height=200)
scroll = Scrollbar(frame4)                                                  # 滚动条
scroll.place(x=225, y=20, width=20, height=200)
delete = Button(frame4, text='Delete', command=remove).place(x=100, y=220, width=100, height=80)            # 删除按钮
account_list.config(yscrollcommand=scroll.set)                              # 列表与滚动条绑定，和上面一样
scroll.config(command=account_list.yview)
for a in Bank_Account_Tasks.accounts_list:                                  # 循环向列表添加数据
    account_list.insert(END, a[5])
root.mainloop()                                                             # 保证程序处于循环运行状态
