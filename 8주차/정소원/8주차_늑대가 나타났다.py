from collections import deque

R, C = map(int, input().split())
ground = [input() for _ in range(R)]
checked = [[False] * C for _ in range(R)]

vertexs = []
for i in range(R):
    for j in range(C):
        if ground[i][j] == "o" or ground[i][j] == "v":
            vertexs.append((i, j))


def bfs(x, y):
    q = deque()
    q.append((x, y))
    checked[x][y] = True
    sheep, wolf = 0, 0
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while len(q) > 0:
        x, y = q.popleft()
        if ground[x][y] == "o":
            sheep += 1
        elif ground[x][y] == "v":
            wolf += 1
        for i in range(4):
            nx, ny = x + mv[i][0], y + mv[i][1]
            if nx >= 0 and nx < R and ny >= 0 and ny < C:
                if ground[nx][ny] != "#" and not checked[nx][ny]:
                    q.append((nx, ny))
                    checked[nx][ny] = True
    return (sheep, wolf)  # 같은 영역에 있는 양과 늑대의 수 반환


sheep, wolf = 0, 0
for x, y in vertexs:
    if not checked[x][y]:
        s, w = bfs(x, y)
        if s > w:
            sheep += s
        else:
            wolf += w
print(sheep, wolf)