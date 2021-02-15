N, M = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False] * N

# 인접행렬
for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)


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
    e, length = dfs(e, 1, 1, e)
    if length == 5:
        print(1)
    else:
        print(0)
