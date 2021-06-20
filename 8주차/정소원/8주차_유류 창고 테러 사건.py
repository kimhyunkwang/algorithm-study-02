# 7주차/8주차 유류 창고 테러 사건(BFS, LEVEL 6)
from copy import deepcopy
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
container, fires = [], []

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 2:
            fires.append((i, j))
    container.append(line)


def ckFinished(box):
    for i in range(n):
        for j in range(n):
            if box[i][j] == 0:
                return False
    return True


def bfs(starts, box):
    res, finished = 0, ckFinished(box)
    q, mv = deque(), [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if finished:
        return res
    for x, y in starts:
        q.append((x, y, 0))
    while len(q) > 0:
        x, y, t = q.popleft()
        for i in range(4):
            nx, ny = x + mv[i][0], y + mv[i][1]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if box[nx][ny] != 1 and box[nx][ny] != 3:
                    box[nx][ny] = 3
                    q.append((nx, ny, t + 1))
        finished = ckFinished(box)
        if finished:
            res = t + 1
            break
    return res if finished else -1


cases = list(combinations(fires, m))
res = float("inf")
for i in range(len(cases)):
    box = deepcopy(container)  # 가연성 물질을 선택하는 케이스 각각에 대한 지도
    for x, y in cases[i]:
        box[x][y] = 3
    res = min(res, bfs(cases[i], box))

if len(cases) == 0:
    print(0)
elif res == float("inf"):
    print(-1)
else:
    print(res)
