import sys

m, n = map(int, input().split())

matrix = [sys.stdin.readline().split() for _ in range(n)]
visited = [[0] * m for _ in range(n)]

queue = []
cnt_infected, cnt_normal, cnt_empty = 0, 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "1":
            queue.append((i, j))
            cnt_infected += 1

        elif matrix[i][j] == "0":
            cnt_normal += 1

        else:
            cnt_empty += 1

if cnt_infected + cnt_empty == n * m:
    print(0)
elif cnt_normal + cnt_empty == n * m:
    print(-1)
else:
    while queue:
        x, y = queue.pop(0)

        if x + 1 < n and visited[x + 1][y] == 0 and matrix[x + 1][y] == "0":
            visited[x + 1][y] = visited[x][y] + 1
            queue.append((x + 1, y))

        if 0 <= x - 1 and visited[x - 1][y] == 0 and matrix[x - 1][y] == "0":
            visited[x - 1][y] = visited[x][y] + 1
            queue.append((x - 1, y))

        if y + 1 < m and visited[x][y + 1] == 0 and matrix[x][y + 1] == "0":
            visited[x][y + 1] = visited[x][y] + 1
            queue.append((x, y + 1))

        if 0 <= y - 1 and visited[x][y - 1] == 0 and matrix[x][y - 1] == "0":
            visited[x][y - 1] = visited[x][y] + 1
            queue.append((x, y - 1))

    print(visited[x][y])


# test case 2번에서 오답이 나오는데 뭐가 문제인지 전혀 모르겠습니다ㅠㅠ
