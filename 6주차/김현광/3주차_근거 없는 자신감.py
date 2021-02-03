# 학생의 수 n과 n명의 점수 입력
value_list = list(map(int, input().split()))

n = value_list[0]
total = sum(value_list) - n
avg = total / n
count = 0

for i in range(n):
    if value_list[i+1] > avg:
        count += 1
answer = count / n * 100

print("%.3f" % answer + "%")