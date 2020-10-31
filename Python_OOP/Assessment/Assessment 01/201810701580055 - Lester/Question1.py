template1 = "{0:<20},{1:>15}"
result1 = template1.format("Escape", "Description")
template2 = "{0:<20},{1:>18}"
result2 = template2.format("_______________", "______________")
template3 = "{0:<20},{1:>22}"
result3 = template3.format("\\n", "New line character")
template4 = "{0:<20},{1:>17}"
result4 = template4.format("\\t", "Tab character")
template5 = "{0:<20},{1:>26}"
result5 = template5.format('\\"',"Double quote character")
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
