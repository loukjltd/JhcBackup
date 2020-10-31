#Task1
"""
id : 201810701580049
class : Net182
name : vivi
"""
template1 = "{0:>16} {1:>30} \n {2} {3:>33}"
result1 = template1.format("Escape sequence", "Description","__________________","__________________")
print(result1)
template2 = "{0:>3} {1:>49} \n {2} {3:>44} \n {4} {5:>53}"
result2 = template2.format("\\n", "New line character","\\t","Tab character",'\\"' , "Double quote character")
print(result2)