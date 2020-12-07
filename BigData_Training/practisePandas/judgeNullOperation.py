import pandas as pds


d1 = {"python": 100, "c++": 300, "c#": 500}
s1 = pds.Series(d1, index=["python", "java", "c#", "c++", "perl"])

print(pds.isnull(s1))
print("-------------------")
print(pds.notnull(s1))
print('\n')

d2 = {"python": 100, "c++": 300, "c#": 500}
s2 = pds.Series(d2, index=["python", "java", "c#", "c++", "perl"])

print(s2.isnull())
print("-------------------")
print(s2.notnull())
