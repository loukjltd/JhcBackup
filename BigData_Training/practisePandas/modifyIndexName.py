import pandas as pds


d = {"python": 100, "c++": 300, "c#": 500}
s = pds.Series(d, index=["python", "java", "c#", "c++", "perl"])

s.index = ["n1", "n2", "n3", "n4", "n5"]
print(s)
