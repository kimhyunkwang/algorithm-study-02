from collections import deque

A, B, C = map(int, input().split())
visited = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]


def getCase(a, b, c):
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
        if na >= 0 and na <= A and nb >= 0 and nb <= B and nc >= 0 and nc <= C:
            res.append((na, nb, nc))
    return res


def bfs(a, b, c):
    q, waters = deque(), []
    q.append((a, b, c))
    visited[a][b][c] = True
    while len(q) > 0:
        a, b, c = q.popleft()
        if a == 0:
            waters.append(c)
        for na, nb, nc in getCase(a, b, c):
            if not visited[na][nb][nc]:
                visited[na][nb][nc] = True
                q.append((na, nb, nc))
    return waters


res = bfs(0, 0, C)
res.sort()
print(*res)