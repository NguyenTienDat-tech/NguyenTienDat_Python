a = "Happiness23424h"
diem = a.lower()
score = {}

for i in diem:
    if i.isalpha():
        if i in score:
            score[i] += 1
        else:
            score[i] = 1
print(score)

