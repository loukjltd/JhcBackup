import pandas as pds

# pds.DataFrame(data, index, columns, dtype, copy)
# data：数据采取各种形式，如: ndarray，series，map，lists，dict，constant和另一个DataFrame。
# index：对于行标签，要用于结果帧的索引是可选缺省值np.arrange(n)，如果没有传递索引值。
# columns：对于列标签，默认与Series相同也是从 0 开始的整数。
# dtype：每列的数据类型
# copy：如果默认值为False，则此命令(或任何它)用于复制数据。

data1 = {"name": ["yahoo", "google", "facebook"], "marks": [200, 400, 800], "price": [90, 80, 70]}

f1 = pds.DataFrame(data1)
print(f1, '\n')

f2 = pds.DataFrame(data1, columns=['name', 'price', 'marks'])
print(f2, '\n')

f3 = pds.DataFrame(data1, columns=['name', 'price', 'marks', 'debts'], index=['01', '02', '03'])
print(f3, '\n')

