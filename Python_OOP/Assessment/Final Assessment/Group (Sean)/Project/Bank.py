# Final Assessment, File: Bank.py
"""
Student Leader Name: Sean
Student ID: 201810701580042
Group Name List: Lee, Shrek, Bruce, Lenny
Pledge of Honour: We pledge by honour that this program is solely our own work.
"""


class Person:  # 定义Person类
    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day):
        # Person类自身包含名，姓，生日的年，月，日
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.birth_month = birth_month
        self.birth_day = birth_day

    def show_details(self):  # show_details方法
        account_details = \
            self.first_name + ',' + self.last_name + ',' + self.birth_year + ',' + \
            self.birth_month + ',' + self.birth_day  # 向account_details中加入名，姓，出生的年，月，日
        return account_details  # 返回这些信息


class Bank_Account(Person):  # 定义Bank_Account类，并继承Person类

    transactions = 0  # 设置总交易笔数为0

    def __init__(self, first_name, last_name, birth_year, birth_month, birth_day, account_id, money, account_type):
        # 包含属性：名，姓，出生的年，月，日，银行账户的ID，金额以及账户类型
        Person.__init__(self, first_name, last_name, birth_year, birth_month, birth_day)
        # 继承的属性包含名，姓，出生的年，月，日
        self.account_id = account_id
        self.money = money
        self.account_type = account_type

    def show_details(self):  # 在Bank_Account类中继续完善具体信息
        if self.account_type == 0:  # 如果银行账户的类型变量为0
            self.account_type = 'Regular'  # 那么该账户类型为普通型
        elif self.account_type == 1:  # 如果银行账户的类型变量为1
            self.account_type = 'Premium'  # 那么该账户类型为高级型
        elif self.account_type == 2:  # 如果银行账户的类型变量为2
            self.account_type = 'Gold'  # 那么该账户类型为黄金型
        account_details = \
            self.first_name + ',' + self.last_name + ',' + self.birth_year + ',' + self.birth_month + ',' + \
            self.birth_day + ',' + self.account_id + ',' + str(self.money) + ',' + self.account_type
        # 向account_details中加入名，姓，出生的年，月，日，银行账户的ID，金额以及账户类型
        return account_details  # 返回这些信息

    def money_in(self, money):  # 设置银行内部有金钱增加的函数
        self.money += float(money)  # 累计存入的金额
        return True  # 累计增加(存款)成功后返回True

    def money_out(self, money):  # 设置银行内部有金钱减少的函数
        self.money -= float(money)  # 累计取出的金额
        if self.money >= 0:  # 如果银行内部的金钱数额大于0
            return True  # 那么返回True表示扣款成功
        else:  # 如果该账户已经没有钱，即金钱输入为0或小于0时
            return False  # 那么返回False便是扣款失败


class BankAccountTasks:  # 定义BankAccountTasks类

    accounts_list = []  # 创建account_list的列表框
    file_name = 'BankAccountInf.txt'  # 将数据存储的文件的名称存到file_name中

    def read_data(self):  # 定义读取数据的方法
        f = open('./BankAccountInf.txt', 'r')  # 打开文本文件
        for line in f.readlines():  # 读取每一行的内容
            split_line = line.split(',')  # 读取的内容通过逗号(,)分隔
            object_first_name = split_line[0]  # 第一项内容为名，存入object_first_name
            object_last_name = split_line[1]  # 第二项内容为姓，存入object_last_name
            object_birth_year = split_line[2]  # 第三项为出生的年，存入object_birth_year
            object_birth_month = split_line[3]  # 第四项为出生的月，存入object_birth_month
            object_birth_day = split_line[4]  # 第五项为出生的日，存入object_birth_day
            object_account_id = split_line[5]  # 第六项为银行账户的ID，存入object_account_id
            object_money = float(split_line[6])  # 第七项为银行账户的金额，存入object_money
            object_account_type = split_line[7]  # 第八项为银行账户的类型，存入object_account_type
            new_object = Bank_Account(
                object_first_name, object_last_name, object_birth_year, object_birth_month, object_birth_day,
                object_account_id, object_money, object_account_type)  # 将这些信息存入new_object，并一一对应具体信息
            self.accounts_list.append(new_object)
        f.close()  # 关闭文件

    def write_data(self):  # 定义写入数据的方法
        f = open('./BankAccountInf.txt', 'w')  # 打开文本文件
        for line in self.accounts_list:  # 读取银行账户
            statement = \
                line.first_name + ',' + line.last_name + ',' + line.birth_year + ',' + line.birth_month + ',' + \
                line.birth_day + ',' + line.account_id + ',' + str(line.money) + ',' + line.account_type
            # 按照格式要求读取出相关内容并用逗号(,)分隔
            f.write(statement)  # 写入
        f.close()  # 关闭文件

    def check_account(self, string_account_id):  # 检查银行账户是否存在的方法
        for line in self.accounts_list:  # 读取银行账户信息
            if string_account_id == line.account_id:  # 如果账户存在
                return 1  # 那么返回1，如果没有就什么都不做

    def put_money_in(self, string_account_id, amount):  # 定义存款的方法
        for line in self.accounts_list:  # 读取银行账户信息
            if string_account_id == line.account_id:  # 如果账户存在
                if line.money_in(amount):  # 调用money_in方法，检查是否存入成功，成功为True
                    line.transactions += 1  # 总交易笔数+1
                    return True  # 存入成功则返回Success
                else:  # 否则...
                    return False  # 存入失败返回Failed

    def put_money_out(self, string_account_id, amount):  # 定义取款的方法
        for line in self.accounts_list:  # 读取银行账户信息
            if string_account_id == line.account_id:  # 如果账户存在
                if line.money_out(amount):  # 调用money_out方法，检查是否取出成功，成功为True
                    line.transactions += 1  # 总交易笔数+1
                    return True  # 取出成功则返回Success
                else:  # 否则...
                    return False  # 取出失败返回Failed

    def show_biggest_account(self):  # 定义显示钱最多的账户的方法
        max_account = self.accounts_list[0]  # 将名存储到max_account中去
        for line in self.accounts_list:  # 读取银行账户信息
            if max_account.money < line.money:  # 如果有金额比之前最大金额的那个人有更大的
                max_account = line  # 则改变名字为到当前金额最大的那个人
        return max_account.show_details()  # 所有比较完成之后，列出该名所在的具体信息

    def most_transactions(self):  # 定义显示交易笔数最多的账户的方法
        max_account = self.accounts_list[0]  # 将名存储到max_account中去
        for line in self.accounts_list:  # 读取银行账户信息
            if max_account.transactions < line.transactions:  # 如果有交易笔数更多的
                max_account = line  # 则改变名字为到当前交易笔数最多的那个人
        return max_account.show_details()  # 所有比较完成之后，列出该名所在的具体信息

    def add_transactions(self, add_transactions_list):  # 定义增加交易笔数的方法
        if len(add_transactions_list) == 0:  # 如果该列表中的长度为0
            return 0  # 返回总交易笔数为0
        else:  # 否则
            new_list = add_transactions_list[1:len(add_transactions_list)]  # 将该列表中的第二项到最后一项添加到新列表中去
            return add_transactions_list[0].transactions + self.add_transactions(new_list)
        # 嵌套循环，有一笔交易曾增加一笔交易

    def get_number_of_transactions(self):  # 定义获取总交易笔数的方法
        self.add_transactions(self.accounts_list)  # 从add_transactions获取最终结果

    def show_account(self, string_account_id):  # 定义显示全部账户的方法
        for show_account_line in self.accounts_list:  # 读取银行账户信息
            if string_account_id == show_account_line.account_id:  # 核对账号后
                return show_account_line  # 返回账号的所在行

    def delete_account(self, string_account_id):  # 定义删除账户的方法
        for delete_account_line in self.accounts_list:  # 读取银行账户信息
            if string_account_id == delete_account_line.account_id:  # 核对账号后
                self.accounts_list.remove(delete_account_line)  # 删除指定账户信息
