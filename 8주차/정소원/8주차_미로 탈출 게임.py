# 6주차/8주차 미로 탈출 게임(BFS, LEVEL 5)
from collections import deque

N = int(input())
maze = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


def bfs(x, y):
    res = float("inf")
    q = deque()
    q.append((x, y, 1))
    visited[x][y] = True
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(q) > 0:
        x, y, d = q.popleft()
        if x == N - 1 and y == N - 1:
            res = min(res, d)
        for i in range(4):
            nx, ny = x + mv[i][0], y + mv[i][1]
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if maze[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, d + 1))
    return res


print(bfs(0, 0))
