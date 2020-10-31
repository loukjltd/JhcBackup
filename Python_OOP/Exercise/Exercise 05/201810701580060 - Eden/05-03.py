'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
student = {"Name":"James","Age":"21","Course":"IT","ID":"2016A001"}
print(student)

Key_value = student["Name"] +":" + student["ID"]
id_value = student["ID"]
print(Key_value)
print(id_value)

del student["Course"]
print(student)

for thing in student:
    print(thing)