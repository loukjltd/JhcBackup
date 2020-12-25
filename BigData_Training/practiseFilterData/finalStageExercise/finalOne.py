# 练习描述：使用pandas 完成对" 前程无忧招聘信息"的数据清洗与可视化
#
# 项目介绍：
# 1.使用pandas导入"前程无忧招聘信息"的数据
#   从本地的csv文件中读取"前程无忧招聘信息"的数据
#
# 2.使用pandas对招聘数据进行清洗
#   删除招聘信息中”公司名+职位名+所在地“相同的数据√
#   筛选数据中”薪资“为万/月的数据。 部分公司使用”千/月、元/天、万/年“为薪资单位，作为异常值被过滤掉
#   将”薪资“列拆分为两个数字列：最低薪资、最高薪资，并合并到原来的数据中
#   将”职位“列的空值全部填充为：python 爬虫工程师
#   将”最低薪资“和”最高薪资“的空值使用平均值填充
#   将”所在地“的值去掉区名，只保留城市
#   删除城市为”异地招聘“的数据
#
# 3.使用 pandas 对清洗后的数据进行分组、统计、排序
#   统计薪资最高的10个公司
#   统计招聘人数最多的前10个城市
#   统计招聘人数最多的10个城市的平均薪资
#
# 4.使用 pandas 对统计数据生成图表保存到本地
#   生成”薪资最高的10个公司“的水平柱状图
#   生成”统计招聘人数最多的前10个城市”饼状图
#   生成”招聘人数最多的10个城市的平均薪资“垂直柱状图

import pandas as pds
import matplotlib as mpl
import matplotlib.pyplot as mpl_plt

pds.set_option('display.max_columns', None)

basicData = pds.read_csv('basicData.csv')
basicData.fillna(value='python 爬虫工程师', inplace=True)
delData = basicData.drop_duplicates(['company_name', 'job_title', 'workplace'], keep='first', inplace=False)
filterData = delData[delData['salary'].str.contains('万/月')]
filterData = filterData[~ filterData['workplace'].str.contains('异地招聘')]


def cut_word_min_salary(word1):
    position1 = word1.find('-')
    min_salary = word1[:position1]
    return min_salary + '万/月'


def cut_word_max_salary(word2):
    position2 = word2.find('-')
    max_salary = word2[position2 + 1:]
    return max_salary


findMinSalary = filterData.salary.apply(cut_word_min_salary)
findMaxSalary = filterData.salary.apply(cut_word_max_salary)

filterData.insert(2, 'min_salary', findMinSalary)
filterData.insert(3, 'max_salary', findMaxSalary)

del filterData['salary']


def cut_area_word(word3):
    for i in word3:
        if i == '-':
            flag = True
        else:
            flag = False

        if flag:
            position3 = word3.find('-')
            delete_area = word3[:position3]
            return delete_area
        elif not flag:
            position3 = 2
            delete_area = word3[:position3]
            return delete_area


deleteArea = filterData.workplace.apply(cut_area_word)

filterData.insert(5, 'workplace_new', deleteArea)
del filterData['workplace']
print(filterData.head(20))
print('*' * 50)

max10Salary = filterData.sort_values(by='max_salary', ascending=False)
print('********************薪资最高的10个公司***************')
print(max10Salary.head(10))
print('*' * 50)

mostPopularCity = filterData['workplace_new'].value_counts()
print('********************招聘人数最多的前10个城市**********')
print(mostPopularCity.head(10))
print('*' * 50)


