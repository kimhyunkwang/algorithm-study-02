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

# Q. 최대 간선의 수(0<=M<=400)가 왜 최대 400개나 되나요...?
# - cycle A-B가 같은 경우가 없으면 자체 사이클이 없으니 중복 된 관계 조합이 없으면 최대 (19*20/2)190개 중복이 있으면 최대 (19*20)380개 아닌가요?
# Q. 코드에서 더 최적화 할 부분이 있는지 리뷰 부탁드립니다!
