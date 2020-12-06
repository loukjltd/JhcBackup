import random
points = []
money = 1000
while money > 0:
    print("****************游戏开始***************")
    for i in range(3):
        point = int(random.randint(1, 6))
        points.append(point)

    a = str(input('请下注，大/小/豹子：'))
    if a not in ('大', '小', '豹子'):
        print("输入错误，重新输入。")
        continue
    c = str
    b = int(input('下注金额：'))
    if b > money or b <= 0:
        print("输入错误，重新输入。")
        continue
    d = points[0]+points[1]+points[2]
    print('********\n* 摇骰子 *\n********')
    print('开：'+str(points))
    if points[0] == points[1] == points[2]:
        c = str('豹子')
    elif 4 <= d <= 10:
        c = str('小')
    elif 11 <= d <= 17:
        c = str('大')
    if a == c and a != '豹子':
        money += b
        print('恭喜你，你赢了'+str(b)+'元，你现在有'+str(money)+'元本金')
    elif a == c and a == '豹子':
        money += b*5
        print('恭喜你，你赢了' + str(b*5) + '元，你现在有' + str(money) + '元本金')
    else:
        money -= b
        print('很遗憾，你输了' + str(b) + '元，你现在有' + str(money) + '元本金')
    points.clear()
print('游戏结束')
