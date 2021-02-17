from collections import deque

N, A, G, U, D = map(int, input().split())
visited = [False] * (N + 1)


def bfs(v):
    q = deque()
    visited[v], finished = True, False
    q.append((v, 0))
    while len(q) > 0:
        v, cnt = q.popleft()
        if v == G:
            finished = True
            break
        up, down = v + U, v - D  # 다음 정점이 될 수 있는 up, down
        if up > 0 and up <= N and not visited[up]:
            q.append((up, cnt + 1))
            visited[up] = True
        if down > 0 and down <= N and not visited[down]:
            q.append((down, cnt + 1))
            visited[down] = True
    if finished:
        print(cnt)
    else:
        print("계단을 사용하세요.")


bfs(A)
