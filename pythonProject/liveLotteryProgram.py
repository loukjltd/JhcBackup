# 导入random模块，用于生成随机数
import random
# 导入time模块，用于计时器
import time

# 欢迎界面
print('**********************')
print('*欢迎来到Lonemm的抽奖程序*')
print('**********************')
# flag用于确认是否开始，finalList用于存储最终获奖名单，times用于存储抽奖次数
flag = False
finalList = []
times = 0

# 如下内容所示
likePlayers = input('请输入已点赞的人数(请输入一个正整数)：')
totalRewards = input('请输入想要抽的奖品总数(请输入一个正整数)：')
areYouSure = input('是否确定开始抽奖(请输入y或者n)：')

# 判断主播是否决定开始抽奖
if areYouSure == 'y':
    flag = True
else:
    flag = False

# 确定开始后生成随机数
if flag:
    while times < int(totalRewards):
        finalList.append(random.randint(1, int(likePlayers)))
        times += 1
    print('')
    print('倒计时开始！')
    for second in range(10, -1, -1):
        print("%02d:%02d" % (second // 60, second % 60))
        time.sleep(1)
    print('')
    print('(中奖信息将重复显示3次)')
    print('中奖的人的序号为' + str(finalList) + '！')
    print('中奖的人的序号为' + str(finalList) + '！')
    print('中奖的人的序号为' + str(finalList) + '！')
    print('')
    input('按下任意按钮以退出。')

# 确定不开始那么退出
else:
    print('您还没有准备好抽奖！')
    print('')
    input('按下任意按钮以退出。')
