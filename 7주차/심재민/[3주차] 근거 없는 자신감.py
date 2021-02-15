# [수학] 근거 없는 자신감

N = list(map(int, input().split()))

score = N[1:]

avg = (sum(score)/N[0])

cnt = 0

for i in score:
    if i > avg:
        cnt += 1

result = (cnt / N[0]) * 100

print('%.3f%s' %(result, '%'))
