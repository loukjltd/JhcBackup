import pandas as pds

s1 = pds.Series([10, 20, 30, 40], index=list('abcd'))


s1['f'] = 100
print(s1)
print('\n')

s2 = pds.Series([10, 20, 30, 40])

s2[5] = 200
print(s2)
print('\n')

s3 = pds.Series([10, 20, 30, 40], index=list('abcd'))
s4 = pds.Series([100, 200], index=['g', 'h'])


print(s3.append(s4))
