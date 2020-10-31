template1 = "{0:<25}{1:>18}"
result1 = template1.format("Escape sequence", "Description")
template2 ="{0:<25}{1:>20}"
result2 = template2.format('__________________','_____________')
template3 = "{0:<25}{1:>25}"
result3 = template3.format('\\n','New line character')
template4 = "{0:<25}{1:>20}"
result4 = template4.format('\\t','Tab character')
template5 = "{0:<25}{1:>29}"
result5 = template5.format('\\"','Double quote character')
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

