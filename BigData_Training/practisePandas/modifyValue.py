import pandas as pds

s = pds.Series([100, "python", False, "loukjltd"], index=["mark", "title", "status", "name"])

# Modify values according to tag index
s["name"] = "loukjltd.online"
s["mark"] = 20

# Modify values according to position subscript
s[1] = "java"

print(s)
