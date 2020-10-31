
'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

template = "{0:<15}  {1:>20}"
result = template.format("Escape sequence" , "Description")
print(result)

template2 = "{0:<21}  {1:>17}"
result2 = template2.format("__________________" , "______________")
print(result2)

templ3 = "{0:<21}  {1:>21}"
result3 = templ3.format("\\""n" , "New line character")
print(result3)

template4 = "{0:<18}  {1:>19}"
result4 = template4.format("\\""t" , "Tab character")
print(result4)

template5 = "{0:<18}  {1:>28}"
result5 = template5.format('\\"' , "Double quote character")
print(result5)