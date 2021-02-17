# 백준 ABCDE와 같은 문제
# https://www.acmicpc.net/problem/13023
# 인접행렬로 푸는 방식 추가예정

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False] * N

# 인접리스트
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# v: 현재 정점, length: 현재까지 탐색한 정점 개수
# mx: 탐색한 length의 최댓값, last: length가 최대였을 때 탐색한 마지막 정점
def dfs(v, length, mx, last):
    if length == 5:
        return (v, length)
    for nxt in adj[v]:
        if not visited[nxt]:
            visited[nxt] = True
            cur = dfs(nxt, length + 1, mx, nxt)
            if cur[1] > mx:
                mx, last = cur[1], cur[0]
            visited[nxt] = False
    return (last, mx)


visited[0] = True
e, length = dfs(0, 1, 1, 0)

if length == 5:
    print(1)
else:
    visited = [False] * N
    visited[e] = True
    e, length = dfs(e, 1, 1, e)
    if length == 5:
        print(1)
    else:
        print(0)
