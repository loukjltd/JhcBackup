import pandas as pds

# Align
d = {"python": 100, "c++": 300, "c#": 500}
s = pds.Series(d, index=["python", "java", "c#", "c++"])
print(s)
