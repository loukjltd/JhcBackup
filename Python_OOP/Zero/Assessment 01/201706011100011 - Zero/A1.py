#201706011100011 ZERO
template = "{0:<7}{1:<23}{2:<11}"
result = template.format("Escape", "sequence","Description")
print(result)

template = "{0:<30}{1:<}"
result = template.format("__________________", "______________")
print(result)

template = "{0:<30}{1:<4}{2:<5}{3:<9}"
result = template.format("\\n", "New","line","character")
print(result)

template = "{0:<30}{1:<4}{2:<9}"
result = template.format("\\t", "Tab","character")
print(result)

template = "{0:<1}{1:<29}{2:<7}{3:<6}{4:<9}"
result = template.format("\\","\"","Double","quote","character")
print(result)


