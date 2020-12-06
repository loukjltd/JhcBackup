score = [75, 98, 59, 81, 66, 43, 69, 85]
total = 0
count = 0

for i in score:
    if i >= 60:
        total = total + i
        count += 1
    continue

print(str(total / count))
