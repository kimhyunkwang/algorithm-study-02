from collections import deque

N, K = map(int, input().split())
cost = list(map(int, input().split()))

# prev: 상위 작업 인접리스트, visited: 중복 검사 리스트
prev, visited = [[] for _ in range(N)], [False] * N
for i in range(K):
    p, c = map(int, input().split())
    prev[c - 1].append(p - 1)
C = int(input())

# v: 현재 탐색하는 vertex, time: 현재까지 시간의 총합, mn: time의 최솟값
def getMinTime(v, time, mn):
    if len(prev[v]) == 0:
        mn = min(time, mn)
        return mn
    nxt, mx = prev[v][0], -1
    for i in range(1, len(prev[v])):
        cur = prev[v][i]
        if cost[cur] > mx:
            mx, nxt = cost[cur], cur
    mn = getMinTime(nxt, time + cost[nxt], mn)
    return mn


print(getMinTime(C - 1, cost[C - 1], float("inf")))
