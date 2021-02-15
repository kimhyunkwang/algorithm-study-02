# [BFS] 자원 절약 운동

# 1 (80점)
n, m = map(int, input().split())
connection = [list(map(int, input().split())) for _ in range(m)]

cnt = [0 for i in range(n)]

s = -1

for i in range(m):
    for j in range(2):
        for k in range(1, n+1):
            if connection[i][j] == k:
                cnt[k-1] += 1
                
res_list = [i for i, value in enumerate(cnt) if value == max(cnt)]

print(res_list[0]+1)

# 2 (80점)
from collections import deque

def bfs(num, n, m, connection):
    i = num # i = 1
    visited = [0] * (n+1)
    conn = connection[:]
    
    dq = deque([[i, 0]])
    # print(dq)
    
    while dq:
        w = dq.popleft() 
        # print(w)
        pointer = w[0] 
        cnt = w[1] + 1 
        for con in conn:
            # print(con)
            if pointer in con:
                temp = con[:] 
                # print(temp)
                temp.remove(pointer) 
                # print(temp)
                dq.append([temp[0], cnt]) 
                conn.remove(con)
                if visited[temp[0]] == 0:
                    visited[temp[0]] = cnt
        # print(visited)
    return sum(visited)

n, m = map(int, input().split())
connection = [list(map(int, input().split())) for _ in range(m)]
# print(connection)
a = 99999
ans_index = 0

for i in range(1, n):
    ans = bfs(i, n, m, connection)
    if a > ans:
        a = ans
        ans_index = i

print(ans_index)