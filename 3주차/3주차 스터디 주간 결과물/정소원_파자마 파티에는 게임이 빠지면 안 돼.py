# 방법1 list를 이용한 반복문처리: 시간초과(40)
N, K, M = map(int, input().split())

q, cur, res = [n for n in range(1,N+1)], 0, 0
while cur != M:
    for i in range(1,K+1):
        cur = q.pop(0)
        if i == K:
            break
        q.append(cur)
    res += 1
print(res)

# 방법2 deque를 이용한 반복문처리: 시간초과(60)
from collections import deque

N, K, M = map(int, input().split())

def findSurvivor(total):
    q, res, find = deque(), 0, False
    for people in range(total):
        q.append(people+1)
    while not find:
        for i in range(K-1):
            cur = q.popleft()
            q.append(cur)
        res += 1
        if q[0] == M:
            find = True
        else:
            q.popleft()
    return res

solution = findSurvivor(N)
print(solution)
# [참조] 실전편 ① 요세푸스 문제 해답|작성자 엘리스코딩

# Q(접근방법). DP를 이용하거나, 특정 규칙을 이용하면 풀릴 것 같은데 딱히 해결방법이 떠오르지 않습니다.
# Q(접근방법). 분류가 queue여서 queue를 이용한 효율적인 풀이가 무엇인지 궁금합니다!
