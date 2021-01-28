# 컴포넌트 개수 세는 문제2
c, r, k = map(int, input().split())
sample = [[0]*c for _ in range(r)]
visited = [[False]*c for _ in range(r)]

cavity = []
for i in range(k):
    y, x = map(int, input().split())
    sample[x][y] = 1
    cavity.append((x, y))


def dfs(x, y):
    mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for mx, my in mv:
        nx, ny = x+mx, y+my
        if nx >= 0 and nx < r and ny >= 0 and ny < c:
            if sample[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)


count = 0
for x, y in cavity:
    if not visited[x][y]:
        visited[x][y] = True
        dfs(x, y)
        count += 1
print(count)
