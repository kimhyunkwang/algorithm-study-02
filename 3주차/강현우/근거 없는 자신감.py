score = list(map(int, input().split()))

score.pop(0)
average = sum(score) / len(score)
good_student = 0

for i in score:
    if i > average:
        good_student += 1

print("{:.3f}%".format(round(good_student/len(score)*100,3)))