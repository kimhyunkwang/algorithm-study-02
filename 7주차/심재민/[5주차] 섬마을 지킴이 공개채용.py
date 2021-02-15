# [BFS] 섬마을 지킴이 공개채용

from collections import deque

m, n, k = map(int, input().split())

maps = [[0]*m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    maps[y][x] = 1
    
def bfs(x, y):
    d = [(1,0), (0,1), (-1,0), (0,-1)]
    
    q = deque()
    q.append((x,y))
    # print(q)
    
    maps[x][y] = 0
    
    while q:
        cur = q.popleft()
        # print(cur)
        
        for i in range(4):
            dx = cur[0] + d[i][0]
            dy = cur[1] + d[i][1]
            # print(dx, dy)
            
            if (0 <= dx < n) and (0 <= dy < m):
                if maps[dx][dy] == 1:
                    maps[dx][dy] = 0
                    q.append((dx,dy))
    
cnt = 0

for x in range(n):
    for y in range(m):
        if maps[x][y] == 1:
            cnt += 1
            bfs(x,y)

print(cnt)