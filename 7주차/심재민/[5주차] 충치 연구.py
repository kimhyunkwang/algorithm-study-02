# [BFS, DFS] 충치 연구

from collections import deque

c, r, k = map(int, input().split())

teeth = [[0]*c for _ in range(r)]
cavity = [[False]*c for _ in range(r)]

for _ in range(k):
    x, y = map(int, input().split())
    teeth[y][x] = 1

def bfs(x,y):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    q = deque()
    q.append((x,y))
    
    teeth[x][y] = 0
    
    while q:
        cur = q.popleft()
        
        for i in range(4):
            dx = cur[0] + directions[i][0]
            dy = cur[1] + directions[i][1]
            
            if (0 <= dx < r) and (0 <= dy < c):
                if teeth[dx][dy] == 1:
                    teeth[dx][dy] = 0
                    q.append((dx,dy))

cnt = 0

for x in range(r):
    for y in range(c):
        if teeth[x][y] == 1:
            cnt += 1
            bfs(x,y)

print(cnt)
