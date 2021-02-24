# 컴포넌트 세는 문제
from collections import deque

M, N, K = map(int, input().split())

ground = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
vertexs = []
for i in range(K):
    x, y = map(int, input().split())
    ground[x][y] = 1
    vertexs.append((x, y))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(q) > 0:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + mv[i][0], y + mv[i][1]
            if nx >= 0 and nx < M and ny >= 0 and ny < N:
                if ground[x][y] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True


duck = 0
for x, y in vertexs:
    if not visited[x][y]:
        bfs(x, y)
        duck += 1
print(duck)
