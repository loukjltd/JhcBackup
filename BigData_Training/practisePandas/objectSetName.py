import pandas as pds

s = pds.Series(range(20))
s.name = "Index Number List"
s.index.name = "INDEX"
print(s)
