score = [95, 97, 74, 63, 66, 94, 93, 97, 76, 93, 89, 70, 69, 97, 61]
count = 0
newScore = []

print(str(len(score)))

for i in score:
    if i == 97:
        count += 1
print(str(count))

score.sort()

del score[0]
del score[0]
print(score)
