N = int(input())
puzzle = [list(map(int, input().split())) for _ in range(N)]
started = [[False for c in range(N)] for r in range(N)]  # start점의 중복 확인을 위한 배열
mv = [[1, 0], [0, 1], [1, 1], [1, -1]]  # 나머지 방향은 어차피 중복됨


def ckValid(x, y):
    return x >= 0 and x < N and y >= 0 and y < N


def bfs(x, y):
    q = [(x, y, puzzle[x][y], 1, d)
         for d in range(4) if ckValid(x+mv[d][0]*3, y+mv[d][1]*3)]
    started[x][y], mx = True, 0
    while len(q) > 0:
        r, c, v, l, d = q.pop(0)
        if l == 4 or v == 0:
            mx = max(mx, v)
        else:
            nr, nc = r+mv[d][0], c+mv[d][1]
            q.append((nr, nc, v*puzzle[nr][nc], l+1, d))

        # 현재 위치가 시작점이 될 수 있다면 q에 넣기
        if not started[r][c]:
            for i in range(4):
                if ckValid(r+mv[i][0]*3, c+mv[i][1]*3):
                    q.append((r, c, puzzle[r][c], 1, i))
                    started[r][c] = True
    return mx


# (0,0) 부터 탐색
print(bfs(0, 0))
