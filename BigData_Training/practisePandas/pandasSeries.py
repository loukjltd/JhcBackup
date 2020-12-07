import pandas as pds

# Use list to create Series
s1 = pds.Series([1, 2, 'loukejia'])
print(s1, '\n')

# Use dictionary to create Series
s2 = pds.Series({'1': 111, '2': 222, '3': 'Sean'})
print(s2, '\n')

# Change the Series type manually
s3 = pds.Series([100, 200, 300, 400], dtype=float)
print(s3, '\n')

# Use the custom index to generate Series
s4 = pds.Series([999, 888, 777, 666], index=['m1', 'm2', 'm3', 'm4'])
print(s4, '\n')

# Convert Series to Python list
s5 = pds.Series(['a', 'b', 'c', 'd'])
newList = s5.tolist()
print(newList)

