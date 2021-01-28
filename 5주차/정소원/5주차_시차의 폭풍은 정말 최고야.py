from collections import deque

l = int(input())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

mv = [
    (-2, -1),
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, -1),
    (2, 1),
    (-1, -2),
    (1, -2),
]  # 8개의 마 이동 방향
visited = [[False] * l for _ in range(l)]  # 중복 이동을 막기 위한 visited 좌표


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y], finished, res = True, False, 0
    while len(q) > 0 and not finished:
        x, y, c = q.popleft()
        for i in range(8):
            nx, ny = x + mv[i][0], y + mv[i][1]
            if nx == ex and ny == ey:  # 도착점에 도달하면 탐색 종료
                finished = True
                res = c + 1
                break
            if nx >= 0 and nx < l and ny >= 0 and ny < l and not visited[nx][ny]:
                q.append((nx, ny, c + 1))  # 다음 좌표의 후보가 되는 점을 큐에 넣는다.
                visited[nx][ny] = True  # 중복되지 않도록 방문 = True로 바꾸기
    print(res)


bfs(sx, sy)
