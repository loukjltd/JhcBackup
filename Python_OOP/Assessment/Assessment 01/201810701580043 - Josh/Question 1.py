#Question 1
#Josh net182 201810701580043

template = '{0:<29}{1}'
res = []
ori = {'Escape sequence': 'Description', '__________________': '______________', '\\n ': 'New line character', '\\t': 'Tab character', '\\"': 'Double quote character'}
for key in ori:
    res.append(template.format(key, ori[key]))

for i in res:
    print(i)
