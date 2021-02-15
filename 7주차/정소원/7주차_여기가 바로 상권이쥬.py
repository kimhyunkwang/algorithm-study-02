from collections import deque

N = int(input())
matrix = [input() for _ in range(N)]
visited = [[False] * N for _ in range(N)]
houses = []


def bfs(x, y):
    q, cnt = deque(), 0
    visited[x][y] = True
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q.append((x, y))

    while len(q) > 0:
        x, y = q.popleft()
        cnt += 1
        for mx, my in mv:
            nx, ny = x + mx, y + my
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                if matrix[nx][ny] == "1" and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    houses.append(cnt)


for i in range(N):
    for j in range(N):
        if matrix[i][j] == "1" and not visited[i][j]:
            bfs(i, j)

houses.sort()
print(len(houses))
for h in houses:
    print(h)
