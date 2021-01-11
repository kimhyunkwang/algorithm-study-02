# [정렬] 안전요원의 임무

N = int(input())

info = []

for _ in range(N):
    age, name = map(str, input().split())
    age = int(age)
    info.append([age, name])

for i in range(N-1):
    for j in range(i+1, N):
        if info[i][0] > info[j][0]:
            info[i], info[j] = info[j], info[i]

for k in info:
    print(*k)

# 나이 순으로 정렬은 했습니다. 
# 하지만 알바펫 순서로 정렬하는 방법을 잘 모르겠습니다...