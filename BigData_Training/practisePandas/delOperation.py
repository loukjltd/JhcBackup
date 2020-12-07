import pandas as pds

s = pds.Series([10, 20, 30, 40], index=list('abcd'))

# Delete elements with drop
print(s.drop('c'))
print('\n')
print(s.drop(['a', 'd']))
print('\n')

# Delete elements with pop
print(s.pop('d'))
print('\n')

# Check original elements
print(s)
