# Final Assessment, File: GUI.py
"""
Student Leader Name: Sean
Student ID: 201810701580042
Group Name List: Lee, Shrek, Bruce, Lenny
Pledge of Honour: We pledge by honour that this program is solely our own work.
"""

from tkinter import *  # 导入tkinter模块
from Bank import BankAccountTasks  # 导入Bank.py文件

bankWindow = Tk()  # 设置bankWindow为窗体名称
bankWindow.title('Bank Account System - Powered by Sean\'s Group - Version 2.2')  # 设置窗体标题
bankWindow.geometry('700x780')  # 设置窗体大小为700x780
bankWindow.iconbitmap('./BankIcon.ico')  # 设置程序的图标
bankWindow.resizable(0, 0)  # 防止窗口大小发生变化

textFrame = Frame(bankWindow, width='70', height='35', pady='20')  # 设置textFrame的宽度和高度，以及边界的Y值
textFrame.pack(side=TOP)  # 打包并设置顶端对齐
buttonFrame = Frame(bankWindow, width='60', height='50', padx='30')  # 设置buttonFrame的宽度和高度，以及边界的X值
buttonFrame.pack(side=LEFT)  # 打包并设置左对齐
numberFrame = Frame(bankWindow, width='60', height='50', padx='10')  # 设置numberFrame的宽度和高度，以及边界的X值
numberFrame.pack(side=LEFT)  # 打包并设置左对齐
listFrame = Frame(bankWindow, width='60', height='50', padx='30')  # 设置listFrame的宽度和高度，以及边界的X值
listFrame.pack(side=LEFT)  # 打包并设置左对齐

mainLabel = Label(textFrame, text='Main Display Screen', font=('Times New Roman', 15, 'bold'))
# 显示Main Display Screen的文字
mainLabel.pack()  # 打包
displayText = Text(textFrame, width='60', height='15', font=('Consolas', 12), background='#ADD8E6')
# 在textFrame中放置displayText的文本框，用于显示主要信息，并设置属性

textScroll = Scrollbar(textFrame)  # 对displayText设置滚动条textScroll
textScroll.pack(side=RIGHT, fill=Y)  # textScroll打包，设置在displayText的右边，并填充Y轴
displayText.configure(yscrollcommand=textScroll.set)  # 更新滚动条，并放置在displayText的旁边
displayText.pack(side=LEFT, fill=BOTH)  # displayText打包，靠左，fill=BOTH使两侧均能跟随文字内容而发生改变
textScroll['command'] = displayText.yview()  # 滚动条垂直滚动
displayText.pack()  # 打包


def press_clear():  # 设置按下C按钮的函数
    typed_account = numberEntry.get()  # 将用户输入的内容(数字)添加到typed_account变量中
    number = len(typed_account)  # 获取输入的内容(数字)的长度，添加到number变量中
    numberEntry.delete(number - 1, END)  # 每按一下C按钮，输入的内容(数字)删除一位


def press_enter():  # 设置按下ENTER按钮的函数
    typed_account = numberEntry.get()  # 将用户输入的内容(数字)添加到typed_account变量中
    displayText.insert(END, typed_account)  # 将输入的内容(数字)添加到displayText的末尾
    numberEntry.delete(0, END)  # 清空numberEntry输入框
    first_line = displayText.get(index1=1.0, index2=1.30)
    # 获取displayText中第1行的开始列到第1行第3列的内容，并存到first_line变量中
    second_line = displayText.get(index1=2.0, index2=2.90)
    # 获取displayText中第2行的开始列到第2行第9列的内容，并存到second_line变量中
    fourth_line = displayText.get(index1=4.0, index2=4.70)
    # 获取displayText中第4行的开始列到第4行第7列的内容，并存到fourth_line变量中

    if first_line == 'Sho':  # 如果first_line的内容是Sho
        if bank.check_account(typed_account) == 1:  # 如果输入的银行账户包含在数据库(txt)中
            i = bank.show_account(typed_account)  # 将该银行账户的所在文本文件的所在的那一行放到i变量中
            displayText.insert(END, '\nName: ' + i.first_name + ' ' + i.last_name + '\n')
            # 在displayText的末尾按格式要求插入姓和名
            displayText.insert(END, 'Birthday: ' + i.birth_year + '/' + i.birth_month + '/' + i.birth_day + '\n')
            # 在displayText的末尾按格式要求插入生日的年月日
            displayText.insert(END, 'Account ID: ' + i.account_id + '\n')
            # 在displayText的末尾按格式要求插入银行账户的ID
            displayText.insert(END, 'Account Type: ' + i.account_type)
            # 在displayText的末尾按格式要求插入银行账户的类型
            displayText.insert(END, 'Money: ' + str(i.money) + '\n')
            # 在displayText的末尾按格式要求插入银行账户的存款(金钱数额)
        else:  # 如果输入的银行账户不在数据库(txt)中
            displayText.insert(END, '\nAccount number ' + typed_account + ' Cannot Be Found.')
            # 在displayText的末尾按格式要求插入该账户找不到

    elif first_line == 'Put':  # 如果first_line的内容不是Sho，是Put
        if fourth_line != 'Enter A':  # 判断前面是否已经输入了金额，如果否
            if second_line == 'Enter The':  # 如果second_line的内容是Enter The
                if bank.check_account(typed_account) == 1:  # 如果输入的银行账户包含在数据库(txt)中
                    displayText.insert(END, '\nEnter Amount:' + '\n')  # 在displayText的末尾告诉用户请输入金额
                else:  # 如果输入的银行账户不在数据库(txt)中
                    displayText.insert(END, '\nAccount Number ' + typed_account + ' Cannot Be Found.')
                    # 在displayText的末尾按格式要求插入该账户找不到
        else:  # 如果输入过了金额，这样设置避免出现输入的金额找不到的情况
            if fourth_line == 'Enter A':  # 如果fourth_line的内容是Enter A
                third_line = displayText.get(index1=3.0, index2=3.5)
                # 获取displayText中第3行的开始列到第3行第5列的内容，并存到third_line变量中
                bank.put_money_in(third_line, typed_account)  # 调用bank.py中的put_money_in函数
                displayText.insert(END, '\nSuccess')  # 在displayText的末尾显示Success

    elif first_line == 'Get':  # 如果first_line的内容不是Sho，是Get
        if fourth_line != 'Enter A':  # 判断前面是否已经输入了金额，如果否
            if second_line == 'Enter The':  # 如果second_line的内容是Enter The
                if bank.check_account(typed_account) == 1:  # 如果输入的银行账户包含在数据库(txt)中
                    displayText.insert(END, '\nEnter Amount:' + '\n')  # 在displayText的末尾告诉用户请输入金额
                else:  # 如果输入的银行账户不在数据库(txt)中
                    displayText.insert(END, '\nAccount Number ' + typed_account + ' Cannot Be Found.')
                    # 在displayText的末尾按格式要求插入该账户找不到
        else:  # 如果输入过了金额，这样设置避免出现输入的金额找不到的情况
            if fourth_line == 'Enter A':  # 如果fourth_line的内容是Enter A
                third_line = displayText.get(index1=3.0, index2=3.5)
                # 获取displayText中第3行的开始列到第3行第5列的内容，并存到third_line变量中
                if bank.put_money_out(third_line, typed_account):  # 调用bank.py中的put_money_out函数，判断是否成功
                    displayText.insert(END, '\nSuccess')  # 成功则在displayText的末尾显示Success
                else:  # 没有成功...
                    displayText.insert(END, '\nFailed')  # 显示Failed


def press_delete():  # 设置按下Delete按钮的函数
    little = accountList.get(accountList.curselection())  # 获取用户通过鼠标点击accountList的账户的ID并存储到little变量中去
    bank.delete_account(accountList.get(accountList.curselection()))  # 调用bank.py中的delete_account函数，删除选中的账户
    bank.write_data()  # 打开txt文本文件，写入删除后的数据
    accountList.delete(0, END)  # 将所有账户从accountList中删除
    delete_f = open('./BankAccountInf.txt', 'r')  # 打开txt文本文件

    for y in delete_f.readlines():  # 列举文本文件中的每一行
        delete_split_line = y.split(',')  # 用逗号(,)分隔开来
        accountList.insert(END, delete_split_line[5])  # 将删除后的所有项重新添加到accountList中

    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, 'Account ')  # 在displayText中插入Account文本
    displayText.insert(END, little)  # 在displayText中插入被删除的账户的ID
    displayText.insert(END, ' Delete.')  # 在displayText中插入Delete文本
    numberEntry.delete(0, END)  # 清空numberEntry输入框


def put_money_in():  # 设置存钱的函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, 'Put Money In...' + '\n')  # 在displayText末尾插入(显示)Put Money In...
    displayText.insert(END, 'Enter The Account ID:' + '\n')  # 在displayText末尾插入(显示)Enter The Account ID:


def get_money_out():  # 设置取钱函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, 'Get Money Out...' + '\n')  # 在displayText末尾插入(显示)Get Money Out...
    displayText.insert(END, 'Enter The Account ID:' + '\n')  # 在displayText末尾插入(显示)Enter The Account ID:
    numberEntry.delete(0, END)  # 清空numberEntry输入框


def show_menu():  # 设置显示菜单函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(1.0, '*************************************************\n')  # 内容
    displayText.insert(END, '*               Bank Account Menu               *\n')  # 内容
    displayText.insert(END, '*************************************************\n')  # 内容
    displayText.insert(END, '1.Menu\n')  # 内容
    displayText.insert(END, '2.Put Money In\n')  # 内容
    displayText.insert(END, '3.Get Money Out\n')  # 内容
    displayText.insert(END, '4.Show Account With Most Money\n')  # 内容
    displayText.insert(END, '5.Show Account With Most Transactions\n')  # 内容
    displayText.insert(END, '6.Show One Account\n')  # 内容
    displayText.insert(END, '7.Show All Accounts\n')  # 内容
    displayText.insert(END, '8.Show Total Number Of Transactions\n')  # 内容
    displayText.insert(END, '9.Exit\n')  # 内容


def show_most_money():  # 设置显示哪个人钱最多的函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, '*****Bank Account With The Most Money*****' + '\n')  # 内容
    numberEntry.delete(0, END)  # 清空numberEntry输入框
    i = bank.show_biggest_account()  # 调用bank.py中的show_biggest_account函数，比较出钱最多的那个账户并存在i中
    money_split_line = i.split(',')  # 读取i账户信息后用逗号(,)分隔出具体信息
    displayText.insert(END, 'Name: ' + money_split_line[0] + ' ' + money_split_line[1] + '\n')
    # 在displayText末尾按照要求显示姓和名
    displayText.insert(END, 'Birthday: ' + money_split_line[2] + '/' + money_split_line[3] + '/' +
                       money_split_line[4] + '\n')
    # 在displayText末尾按照要求显示生日
    displayText.insert(END, 'Account ID: ' + money_split_line[5] + '\n')
    # 在displayText末尾按照要求显示银行账户的ID
    displayText.insert(END, 'Account Type: ' + money_split_line[7])
    # 在displayText末尾按照要求显示银行账户的类型
    displayText.insert(END, 'Money: ' + money_split_line[6] + '\n')
    # 在displayText末尾按照要求显示银行账户的金额


def show_most_transactions():  # 设置显示最多交易笔数账户的函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, '*****Bank Account With The Most Transactions*****' + '\n')  # 内容
    numberEntry.delete(0, END)  # 清空numberEntry输入框
    i = bank.most_transactions()  # 调用bank.py中的most_transactions函数，比较出交易笔数最多的那个账户并存在i中
    transactions_split_line = i.split(',')  # 读取i账户信息后用逗号(,)分隔出具体信息
    displayText.insert(END, 'Name: ' + transactions_split_line[0] + ' ' + transactions_split_line[1] + '\n')
    # 在displayText末尾按照要求显示名，姓
    displayText.insert(END, 'Birthday: ' + transactions_split_line[2] + '/' + transactions_split_line[3] + '/' +
                       transactions_split_line[4] + '\n')
    # 在displayText末尾按照要求显示生日
    displayText.insert(END, 'Account ID: ' + transactions_split_line[5] + '\n')
    # 在displayText末尾按照要求显示银行账户的ID
    displayText.insert(END, 'Account Type: ' + transactions_split_line[7])
    # 在displayText末尾按照要求显示银行账户的类型
    displayText.insert(END, 'Money: ' + transactions_split_line[6] + '\n')
    # 在displayText末尾按照要求显示银行账户的金额


def show_one_account():  # 设置显示指定一个账户的函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, 'Show One Account...' + '\n')  # 在displayText末尾插入Show One Account...
    displayText.insert(END, 'Enter The Account ID： ' + '\n')  # 在displayText末尾插入Enter The Account ID：
    numberEntry.delete(0, END)  # 清空numberEntry输入框


def show_all_accounts():  # 设置显示所有账户的函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, 'Showing All Accounts...' + '\n')  # 在displayText末尾插入Showing All Accounts...
    numberEntry.delete(0, END)  # 清空numberEntry输入框
    for i in bank.accounts_list:  # 用i来列举accounts_list的每一个账户，分别输出以下内容
        displayText.insert(END, 'Name: ' + i.first_name + ' ' + i.last_name + '\n')
        # 在displayText末尾按照要求显示姓和名
        displayText.insert(END, 'Birthday: ' + i.birth_year + '/' + i.birth_month + '/' + i.birth_day + '\n')
        # 在displayText末尾按照要求显示生日
        displayText.insert(END, 'Account ID: ' + i.account_id + '\n')
        # 在displayText末尾按照要求显示银行账户的ID
        displayText.insert(END, 'Account Type: ' + i.account_type)
        # 在displayText末尾按照要求显示银行账户的类型
        displayText.insert(END, 'Money: ' + str(i.money) + '\n')
        # 在displayText末尾按照要求显示银行账户的金额
        displayText.insert(END, '**********' '\n')
        # 在displayText末尾插入分割线


def show_total_transactions():  # 设置显示所有账户交易笔数的函数
    displayText.delete('0.0', END)  # 清空displayText内容
    displayText.insert(END, 'Total Transactions：' + '\n')  # 在displayText末尾插入总交易笔数
    numberEntry.delete(0, END)  # 清空numberEntry输入框
    displayText.insert(END, bank.add_transactions(bank.accounts_list))


def exit_bank():  # 设置退出按钮的函数
    bankWindow.destroy()  # destroy表示直接退出


functionLabel = Label(buttonFrame, text='Function Button', font=('Times New Roman', 15, 'bold'))
# 显示Function Button的文字
functionLabel.pack()  # 打包

button1 = Button(buttonFrame, text='Menu', width='30', height='2',
                 command=show_menu, background='#FFFFE0')  # 设置Menu按钮
button2 = Button(buttonFrame, text='Put Money In', width='30', height='2',
                 command=put_money_in, background='#FFFFE0')  # 设置Put Money In按钮
button3 = Button(buttonFrame, text='Get Money Out', width='30', height='2',
                 command=get_money_out, background='#FFFFE0')  # 设置Get Money Out按钮
button4 = Button(buttonFrame, text='Show Account With Most Money', width='30', height='2',
                 command=show_most_money, background='#FFFFE0')  # 设置Show Account With Most Money按钮
button5 = Button(buttonFrame, text='Show Account With Most Transactions', width='30', height='2',
                 command=show_most_transactions, background='#FFFFE0')  # 设置Show Account With Most Transactions按钮
button6 = Button(buttonFrame, text='Show One Account', width='30', height='2',
                 command=show_one_account, background='#FFFFE0')  # 设置Show One Account按钮
button7 = Button(buttonFrame, text='Show All Accounts', width='30', height='2',
                 command=show_all_accounts, background='#FFFFE0')  # 设置Show All Accounts
button8 = Button(buttonFrame, text='Show Total Number Of Transactions', width='30', height='2',
                 command=show_total_transactions, background='#FFFFE0')  # 设置Show Total Number Of Transactions按钮
button9 = Button(buttonFrame, text='Exit', width='30', height='2',
                 command=exit_bank, background='#FFB6C1')  # 设置Exit按钮
button1.pack()  # 打包
button2.pack()  # 打包
button3.pack()  # 打包
button4.pack()  # 打包
button5.pack()  # 打包
button6.pack()  # 打包
button7.pack()  # 打包
button8.pack()  # 打包
button9.pack()  # 打包


display = StringVar()  # 保存一个String类型变量display, 默认值为""(空)，该变量可变
numberEntry = Entry(numberFrame, width=13, textvariable=display,
                    background='#ADD8E6', font=('Times New Roman', 20, 'bold'))  # numberEntry输入框，设置输入框的属性
numberEntry.grid(row=0, column=0, rowspan=2, columnspan=30)
# 通过grid打包放置numberEntry的位置，并设置属性
# row为行数值，column为列数值，rowspan表示横跨多少行，columnspan表示横跨多少列

blankLabel = Label(numberFrame, text='', font=('Arial', 15, 'bold'))
# 用于分隔输入框与数字键
blankLabel.grid(row=2, column=0, columnspan=30)  # 打包

Button(numberFrame, text='1', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字1按钮
       command=lambda: numberEntry.insert(INSERT, '1')).grid(row=3, column=0, columnspan=3)
Button(numberFrame, text='2', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字2按钮
       command=lambda: numberEntry.insert(INSERT, '2')).grid(row=3, column=4, columnspan=3)
Button(numberFrame, text='3', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字3按钮
       command=lambda: numberEntry.insert(INSERT, '3')).grid(row=3, column=8, columnspan=3)
Button(numberFrame, text='4', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字4按钮
       command=lambda: numberEntry.insert(INSERT, '4')).grid(row=4, column=0, columnspan=3)
Button(numberFrame, text='5', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字5按钮
       command=lambda: numberEntry.insert(INSERT, '5')).grid(row=4, column=4, columnspan=3)
Button(numberFrame, text='6', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字6按钮
       command=lambda: numberEntry.insert(INSERT, '6')).grid(row=4, column=8, columnspan=3)
Button(numberFrame, text='7', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字7按钮
       command=lambda: numberEntry.insert(INSERT, '7')).grid(row=5, column=0, columnspan=3)
Button(numberFrame, text='8', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字8按钮
       command=lambda: numberEntry.insert(INSERT, '8')).grid(row=5, column=4, columnspan=3)
Button(numberFrame, text='9', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字9按钮
       command=lambda: numberEntry.insert(INSERT, '9')).grid(row=5, column=8, columnspan=3)
Button(numberFrame, text='C', width=6, height=3, font=('Arial', 12, 'bold'), background='#FFB6C1',  # 放置C按钮
       command=press_clear).grid(row=6, column=0, columnspan=3)
Button(numberFrame, text='0', width=6, height=3, font=('Arial', 12, 'bold'), background='#ADD8E6',  # 放置数字0按钮
       command=lambda: numberEntry.insert(INSERT, '0')).grid(row=6, column=4, columnspan=3)
Button(numberFrame, text='ENTER', width=6, height=3, font=('Arial', 12, 'bold'), background='#90EE90',  # 放置ENTER按钮
       command=press_enter).grid(row=6, column=8, columnspan=3)

accountLabel = Label(listFrame, text='Accounts', font=('Times New Roman', 15, 'bold'))  # 放置右侧列表上的Accounts的Label
accountLabel.pack()  # 打包
accountList = Listbox(listFrame, width=18, height=14, background='#ADD8E6', font=('Arial', 12))
# 放置右侧的列表accountList

listScroll = Scrollbar(listFrame)  # 为列表添加滚动条listScroll
listScroll.pack(side=RIGHT, fill=Y)  # listScroll打包，设置在右边，并填充Y轴
accountList.configure(yscrollcommand=listScroll.set)  # 更新滚动条，并放置在accountList的旁边
listScroll['command'] = accountList.yview()  # 滚动条垂直滚动
accountList.pack(side=LEFT, fill=BOTH)  # accountList打包，设置在左边，fill=BOTH使两侧均能跟随文字内容而发生改变

deleteButton = Button(bankWindow, text='Delete', font=('Arial', 12, 'bold'), background='#FFB6C1', command=press_delete)
# 放置Delete的按钮并设置其属性
deleteButton.place(x=555, y=735, anchor=W, width=75, height=35)
# 使用place确定Delete按钮的位置，x表示x轴坐标，y表示y轴坐标，anchor表示方向(这里的W表示West，即西边)，width和height表示宽度和高度

f = open('./BankAccountInf.txt', 'r')  # 打开文件
for x in f.readlines():  # 用x列举每一行的内容
    split_line = x.split(',')  # 用逗号(,)分隔开来
    accountList.insert(END, split_line[5])  # 向accountList的列表中添加内容

displayText.insert(1.0, '*************************************************\n')  # 欢迎语
displayText.insert(END, '*         Welcome to use Sean\'s Bank!           *\n')  # 欢迎语
displayText.insert(END, '*************************************************\n')  # 欢迎语
displayText.insert(END, 'This bank will provide you: ' + '\n')  # 欢迎语
displayText.insert(END, 'Secure Protection,' + '\n')  # 欢迎语
displayText.insert(END, 'Warm-hearted Service, ' + '\n')  # 欢迎语
displayText.insert(END, 'And a lot of Money!' + '\n')  # 欢迎语
displayText.insert(END, '*************************************************\n')  # 欢迎语
displayText.insert(END, 'Please select the function to start!\n')  # 欢迎语
displayText.insert(END, 'If you have any problem, please click the Menu Button.\n')  # 欢迎语

bank = BankAccountTasks()  # 将BankAccountTasks的类存储到bank中以方便在GUI.py中调用
bank.read_data()  # 调用read_data读取内容

bankWindow.mainloop()  # 开启窗体的循环
