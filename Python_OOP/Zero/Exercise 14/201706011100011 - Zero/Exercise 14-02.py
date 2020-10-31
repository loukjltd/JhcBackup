# net171-ZhaoYinting

f = open("my_text2.txt", "r")
sum_number = 0
for x in f.readlines():
    sum_number += int(x)
print("Sum:", sum_number)
