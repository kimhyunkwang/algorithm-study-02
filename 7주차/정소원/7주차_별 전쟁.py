from collections import deque

N, K = map(int, input().split())
cost = list(map(int, input().split()))

prev, visited = [[] for _ in range(N)], [False] * N
for i in range(K):
    p, c = map(int, input().split())
    prev[c - 1].append(p - 1)
C = int(input())


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
