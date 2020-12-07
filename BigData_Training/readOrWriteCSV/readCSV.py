import pandas as pds
df = pds.read_csv("weather.csv")
df1 = pds.read_csv("weather.csv", usecols=[0, 2, 4], nrows=10)
print(df, '\n')
print(df1, '\n')


df2 = pds.read_csv("weather.csv", header=None, prefix="A")
df3 = pds.read_csv("weather.csv", usecols=["city", "wind"], nrows=None)
print(df2, '\n')
print(df3, '\n')

