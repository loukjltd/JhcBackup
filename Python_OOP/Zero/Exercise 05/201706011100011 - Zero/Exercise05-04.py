#net171 wuzhengbo
marks={"Sam ":90.5,"Jane":85.4,"Max":92.3,"Alice":64.5,"John":69.4 }
sum=0
for i in marks:
    sum+=marks[i]
print("Sum:",sum)
average=sum/len(marks)
print("Average: ",average)