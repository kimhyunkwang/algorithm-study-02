# N개의 지역에 대해 bfs 돌려서 최소 단계 쓰기 / 가중치 있었으면 N번 다익스트라 돌리면 될 듯
# 대체 왜 간선의 수가 최대 400개나 되는가...? cycle 없으면 190개 아닌가..?(의문)
from collections import deque

n, m = map(int, input().split())
# 인접행렬 만들기
adj = [[] for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [False] * (n + 1)  # 방문 체크 배열
    visited[start] = True  # 시작점의 방문여부 등록
    res = 0
    while len(q) > 0:
        v, l = q.popleft()
        res += l
        for u in adj[v]:
            if not visited[u]:  # 방문하지 않은 지역일 경우에만 q에 넣기
                q.append((u, l + 1))
                visited[u] = True
    return res


mn, ans = n + 1, -1
for i in range(n):
    cur = bfs(i + 1)
    if mn > cur:  # 최단 총 운송 단계 수보다 더 적은 값이면
        ans = i + 1  # answer에 해당 지역 넣기
        mn = cur  # 최솟값 바꾸기
print(ans)
