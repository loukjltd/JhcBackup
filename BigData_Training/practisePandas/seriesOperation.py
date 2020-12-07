import pandas as pds

# Pandas Series select operation
s = pds.Series([10, 20, 30, 40], index=list('wxyz'))
print(s)
print('\n')

# Query with position
print(s[2])
print('\n')

# Query with index tag
print(s['x'])
print('\n')

# Query multi-elements
print(s[[0, 2, 3]])
print(s[['w', 'y', 'z']])
print('\n')

# slide
print(s[1:3])
print(s['x':'z'])
print('\n')

# boolean index
print(s[s > 20])
print('\n')
