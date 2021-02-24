from collections import deque

n, k = map(int, input().split())

if n >= k:
    print(n-k)
else:
    que = deque()
    que.append((n, 0))
    visited = [0 for _ in range(100001)]

    while (que):
        cur, time = que.popleft()
        
        nxt = [cur * 3, cur + 1, cur - 1]
        
        if k in nxt:
            print(time + 1)
            break

        for i in range(3):
            if 1 <= nxt[i] <= 100000 and visited[nxt[i]] == 0:
                visited[nxt[i]] = 1
                que.append((nxt[i], time + 1))