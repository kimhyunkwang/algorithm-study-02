# 무어의 법칙[Moore’s Law]

N = int(input())

record = str(2 ** N)

answer = 0

for i in record:
    answer += int(i)

print(answer)