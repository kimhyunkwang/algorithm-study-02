# [BFS] 시차의 폭풍은 정말 최고야!

from collections import deque

l = int(input())
xs, ys = map(int, input().split())
xg, yg = map(int, input().split())

chess = [[0 for _ in range(l)] for _ in range(l)]

x_move = [-1, 1, 2, 2, 1, -1, -2, -2]
y_move = [-2, -2, -1, 1, 2, 2, 1, -1]

def bfs(xs, ys, xg, yg):
    
    q = deque()
    q.append([xs, ys])
    
    chess[xs][ys] = 1
    
    while q:
                
        cur_x, cur_y = q.popleft()
        
        if (cur_x == xg) and (cur_y == yg):
            return chess[cur_x][cur_y] - 1
        
        for i in range(len(x_move)):
            nxt_x = cur_x + x_move[i]
            nxt_y = cur_y + y_move[i]
            if (nxt_x >= 0) and (nxt_y >= 0):
                if (nxt_x < l) and (nxt_y < l):
                    if chess[nxt_x][nxt_y] == 0:
                        q.append([nxt_x, nxt_y])
                        chess[nxt_x][nxt_y] = chess[cur_x][cur_y] + 1

print(bfs(xs, ys, xg, yg))
        