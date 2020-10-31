'''
student name: Yakira
ID: 201810701580034
Pledge of Honour: I pledge by honour that this program is solely my own work.
'''

country = {"Australia":22.5,"China":36.4,"Malaysia":38.4,"New Zealand":18.2}
print("Malaysia" + ": " + str(country["Malaysia"]))
print("China" + ": " + str(country["China"]))
print("Australia" + ": " + str(country["Australia"]))
print("New Zealand" + ": " + str(country["New Zealand"]))
average = sum(country.values())/4
print("Average temperature: "+ str("%.2f"% average))
maximum = max(country.values())
print("Maximum temperature: " + str("%.2f"% maximum))
t = 0
for i in country.values():
    while i > 20 and i < 30:
        t = t + 1
        break
print("Number of temperatures between 20 and 30: ", str(t))