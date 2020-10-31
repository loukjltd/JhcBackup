'''
class:Computer Network 182
ID:201810701580049
chinese name:Zhu gaoxian en:vivi
Exercise 01-04
'''
#"Name"     "Score"
template2 = "{0:>6}  {1:>10} "
result = template2.format("Name","Score")
template2_1 = "{0:>6}  {1:>10}"
result2_1 = template2_1.format("Max","77.2")
result2_2 = template2_1.format("Alice" ,"89.3")
result2_3 = template2_1.format("Bob","68.0")
print(result)
print(result2_1)
print(result2_2)
print(result2_3)