'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
template1 = "{0:<10},{1:>25}"
result = template1.format("Escape sequence", "Description")
print(result) # output: Escape sequence                  Description
template2 = "{0:<10},{1:>26}"
result = template2.format("___________________", "________________")
print(result) # output: ___________________            ________________
template3 = "{0:<10},{1:>37}"
result = template3.format("\\n", "New line character")
print(result) # output: \n                 New line character
template4 = "{0:<10},{1:>32}"
result = template4.format("\\t", "Tab character")
print(result) # output: \t                Tab character
template5 = "{0:<10},{1:>41}"
result = template5.format('\\"',"Double quote character")
print(result) # output: \\"            Double quote character