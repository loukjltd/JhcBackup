'''
student name: Eden
#ID: 201810701580060
#class: net182
'''
radius = float(input("Enter the radius:  "))

def calculate_area(radius):
    return radius * radius * 3.14
def calculate_Perimeter(radius):
    return radius * 2 * 3.14

print("Radius    " + "Area    " + "Perimeter    ")
print("-----------------------------")
print(radius,end="      ")
print(calculate_area(radius),end="    ")
print(calculate_Perimeter(radius),end="    ")