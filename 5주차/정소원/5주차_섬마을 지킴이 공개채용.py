# 그래프 component 수 세는 문제 - 단골로 등장하는 기출문제
import sys
from collections import deque
m, n, k = map(int, sys.stdin.readline().split())
matrix = [[0]*n for _ in range(m)]
visited = [[False]*n for _ in range(m)]
ground = []


def bfs(x, y):
    q = deque()
    q.append((x, y))
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[x][y] = True
    while len(q) > 0:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx+mv[i][0], cy+mv[i][1]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if matrix[nx][ny] == 1 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True


for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    matrix[x][y] = 1
    ground.append((x, y))

res = 0
for x, y in ground:
    if not visited[x][y]:
        bfs(x, y)
        res += 1
print(res)
