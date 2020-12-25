#   基于 Numpy + matplotlib 对苹果公司股价分析和可视化
#   Network 182 - Sean Lou
#   说明：本阶段作业均使用 PyCharm 完成，未使用 Jupyter Book，故没有相关 NoteBook 文件。
#   本文件已共享至 GitHub，详情请见：
#   https://github.com/loukjltd/Jinhua_Polytechnic_class_code_backup/blob/main/BigData_Training/finalPraticalExercise/finalOneExercise.py
#
#   目标要求：
# 1.使用 urllib + re 实现爬虫：从”英为财情“网爬取苹果公司最近一个月的股票历史数据
#
# 2.基于 numpy 分析苹果公司的股票价格
#   求收盘价的算数平均值，加权平均值（用成交量来加权平均价格）
#   求收盘价的最大值，最小值，中位数，方差
#   求每天的收益率，每日收益的标准差
#   看看哪些天的收益率是正的
#   看看周一至周五的平均收盘价，周几的平均收盘价最高，周几的最低
#
# 3.使用 matplotlib 对苹果股票的数据可视化
#   本月股票价格走势图（历史收盘价）
#   本月股票成交量的时间序列图
#   本月每日收益率
#   本月股价最高，最低水平柱状图
#   周一至周五的成交量占比

import urllib.request
import ssl
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import datetime

# 设置 matplotlib 为中文字体，使其能够正常显示中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
# 设置 matplotlib 相关属性，使其能够正常显示负号
mpl.rcParams['axes.unicode_minus'] = False

# 关闭爬取页面的证书验证，使其能够正常访问
ssl._create_default_https_context = ssl._create_unverified_context
# 伪装成浏览器正常访问，阻止生成 403 错误
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url='https://cn.investing.com/equities/apple-computer-inc-historical-data',
                             headers=headers)
# 读取页面
websiteBuff = urllib.request.urlopen(req).read()
# 改变页面编码为 UTF-8
htmlCode = websiteBuff.decode("utf8")

# 爬取日期相关代码，存储到 releaseDateData 中
releaseDateDataCode = 'class="first left bold noWrap">(.+)</td>'
releaseDateDataNormalList = re.findall(releaseDateDataCode, htmlCode)
releaseDateData = np.array(releaseDateDataNormalList)
print(releaseDateData)

# 爬取收盘价相关代码，存储到 closingData 中
closingDataCode = '<td data-real-value="(.+)" class="(.+)Font">(.+)</td>'
closingDataNormalList = re.findall(closingDataCode, htmlCode)
closingData = np.array(list(zip(*closingDataNormalList))[0])
closingData = closingData.astype('float')
print(closingData)

# 爬取交易量相关代码，存储到 turnoverData 中
turnoverDataCode = '<td data-real-value="(.+)">(.+)M</td>'
turnoverDataNormalList = re.findall(turnoverDataCode, htmlCode)
turnoverData = np.array(list(zip(*turnoverDataNormalList))[1])
turnoverData = turnoverData.astype('float')
print(turnoverData)

# 爬取涨跌幅相关代码，存储到 priceLimitData 中
priceLimitDataCode = '<td class="bold (.+)Font">(.+)%</td>'
priceLimitDataNormalList = re.findall(priceLimitDataCode, htmlCode)
priceLimitData = np.array(list(zip(*priceLimitDataNormalList))[1])
priceLimitData = priceLimitData.astype('float')
print(priceLimitData)

# 以下为样式数据，供前期调试使用，现在已不再使用
# # 日期
# releaseDateData1 = np.array(['2020年12月21日', '2020年12月18日', '2020年12月17日', '2020年12月16日', '2020年12月15日',
#                             '2020年12月14日', '2020年12月11日', '2020年12月10日', '2020年12月9日', '2020年12月8日',
#                             '2020年12月7日', '2020年12月4日', '2020年12月3日', '2020年12月2日', '2020年12月1日',
#                             '2020年11月30日', '2020年11月27日', '2020年11月25日', '2020年11月24日', '2020年11月23日'])
# # 收盘
# closingData1 = np.array([128.23, 126.65, 128.7, 127.81, 127.88, 121.78, 122.41, 123.24, 121.78, 124.38,
#                         123.75, 122.25, 122.94, 123.08, 122.72, 119.05, 116.59, 116.03, 115.17, 113.85])
#
# # 交易量
# turnoverData1 = np.array([121.25, 192.54, 94.36, 96.93, 157.57, 79.08, 86.94, 81.31, 115.09, 82.23, 86.71,
#                          78.26, 78.97, 89, 125.92, 167.2, 46.69, 76.5, 113.87, 127.96])
#
# # 涨跌幅
# priceLimitData1 = np.array([1.24, -1.59, 0.70, -0.05, 5.01, -0.51, -0.67, 1.20, -2.09, 0.51, 1.23, -0.56,
#                            -0.11, 0.29, 3.08, 2.11, 0.48, 0.75, 1.16, -2.97])

meanClosingNum = closingData.mean()
print('收盘价的算术平均数是：' + str(meanClosingNum) + '\n')

averageClosingNum = np.average(closingData, weights=turnoverData)
print('收盘价的加权平均数是：' + str(averageClosingNum) + '\n')

maxClosingNum = np.max(closingData)
print('收盘价的最大值是：' + str(maxClosingNum) + '\n')

minClosingNum = np.min(closingData)
print('收盘价的最小值是：' + str(minClosingNum) + '\n')

mediumClosingNum = np.median(closingData)
print('收盘价的中位数是：' + str(mediumClosingNum) + '\n')

varClosingNum = np.var(closingData)
print('收盘价的方差是：' + str(varClosingNum) + '\n')

print('每天的收益率是：')
day1 = 0
for i in releaseDateData:
    print(i, ': ', priceLimitData[day1], '%', sep='')
    day1 += 1
print('\n')

print('每天的收益率的标准差是：')
print(np.std(priceLimitData))
print('\n')

print('这些天的收益是正数：')
day2 = 0
for i in priceLimitData:
    if i > 0:
        print(releaseDateData[day2], ': ', i, '%', sep='')
    day2 += 1

# 股票收盘价折线走势图
closingReverseData = np.sort(closingData)
closingReverseList = closingReverseData.tolist()

releaseDateReverseData = np.sort(releaseDateData)
releaseDateReverseList = releaseDateReverseData.tolist()

plt.plot(closingReverseList, label='收盘价')
plt.xticks(range(len(releaseDateReverseList)), releaseDateReverseList, rotation=45)
plt.legend(loc='upper left')

plt.title('股票收盘价折线走势图')
plt.xlabel('日期')
plt.ylabel('收盘价')
plt.grid(True)
plt.show()

# 股票成交量折线走势图
turnoverReverseData = np.sort(turnoverData)
turnoverReverseList = turnoverReverseData.tolist()

plt.plot(turnoverReverseList, label='成交量')
plt.xticks(range(len(releaseDateReverseList)), releaseDateReverseList, rotation=45)
plt.legend(loc='upper left')

plt.title('股票成交量折线走势图')
plt.xlabel('日期')
plt.ylabel('成交量')
plt.grid(True)
plt.show()

# 股票收益率/涨跌幅柱状图
priceLimitReverseData = np.sort(priceLimitData)
priceLimitReverseList = priceLimitReverseData.tolist()

plt.bar(releaseDateReverseList, priceLimitReverseList)
plt.xticks(range(len(releaseDateReverseList)), releaseDateReverseList, rotation=45)

plt.title('股票收益率/涨跌幅柱状图')
plt.xlabel('日期')
plt.ylabel('收益率/涨跌幅')
plt.show()

# 股票最高/最低收益率柱状图
maxAndMin = np.array([])
maxAndMinDate = np.array([])

maxPriceLimit = np.max(priceLimitData)
maxAndMin = np.append(maxAndMin, maxPriceLimit)
minPriceLimit = np.min(priceLimitData)
maxAndMin = np.append(maxAndMin, minPriceLimit)

day3 = 0
for i in releaseDateData:
    if priceLimitData[day3] == maxPriceLimit:
        maxAndMinDate = np.append(maxAndMinDate, i)
    day3 += 1

day4 = 0
for j in releaseDateData:
    if priceLimitData[day4] == minPriceLimit:
        maxAndMinDate = np.append(maxAndMinDate, j)
    day4 += 1

maxAndMinList = maxAndMin.tolist()
maxAndMinDateList = maxAndMinDate.tolist()

plt.bar(maxAndMinDateList, maxAndMinList)
plt.xticks(range(len(maxAndMinDateList)), maxAndMinDateList, rotation=30)

plt.title('股票最高/最低收益率柱状图')
plt.xlabel('日期')
plt.ylabel('收益率/涨跌幅')
plt.show()

# 周一至周五成交量饼图
weekData = np.array([])
for day in releaseDateData:
    weekData = np.append(weekData, datetime.strptime(day, '%Y年%m月%d日').weekday() + 1)


def weekClosing(target_week):
    day100 = 0
    total_closing_data = 0
    for i_mon in closingData:
        if weekData[day100] == target_week:
            total_closing_data += i_mon
        day100 += 1
    return total_closing_data


closingDataWeek = np.array([])
closingDataWeek = np.append(closingDataWeek, weekClosing(1))
closingDataWeek = np.append(closingDataWeek, weekClosing(2))
closingDataWeek = np.append(closingDataWeek, weekClosing(3))
closingDataWeek = np.append(closingDataWeek, weekClosing(4))
closingDataWeek = np.append(closingDataWeek, weekClosing(5))

weekLabel = ['周一', '周二', '周三', '周四', '周五']

plt.pie(closingDataWeek, labels=weekLabel)
plt.title('周一至周五成交量饼图')
plt.show()
