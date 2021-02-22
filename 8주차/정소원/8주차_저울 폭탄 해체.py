from collections import deque

A, B, C = map(int, input().split())
visited = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]


def getCase(a, b, c):
    # 물을 옮기는 모든 경우의 수
    case = [
        (0, a + b, c),
        (0, b, a + c),
        (a - B + b, B, c),
        (a - C + c, b, C),
        (a + b, 0, c),
        (a, 0, b + c),
        (A, b - A + a, c),
        (a, b - C + c, C),
        (a + c, b, 0),
        (a, b + c, 0),
        (A, b, c - A + a),
        (a, B, c - B + b),
    ]
    res = []
    for na, nb, nc in case:
        # 모든 경우의 수에서 유효한 좌표값만 추려서 반환
        if na >= 0 and na <= A and nb >= 0 and nb <= B and nc >= 0 and nc <= C:
            res.append((na, nb, nc))
    return res


def bfs(a, b, c):
    q, waters = deque(), []
    q.append((a, b, c))
    visited[a][b][c] = True
    while len(q) > 0:
        a, b, c = q.popleft()
        if a == 0:  # 문제에서 원하는 A의 물통이 비었을 때만, 배열에 추가
            waters.append(c)
        for na, nb, nc in getCase(a, b, c):
            if not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                q.append((na, nb, nc))
    return waters


res = bfs(0, 0, C)
res.sort()
print(*res)