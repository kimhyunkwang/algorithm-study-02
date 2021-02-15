import sys

N = int(input())
snow = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
S = [[-1] * N for _ in range(N)]
distance = [[-1] * N for _ in range(N)]
mv = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def getDistance(x, y):
    if distance[x][y] != -1:
        return (S[x][y], distance[x][y])
    S[x][y], distance[x][y] = snow[x][y], 1
    for mx, my in mv:
        nx, ny = x + mx, y + my
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if snow[nx][ny] >= snow[x][y]:
                s, d = getDistance(nx, ny)
                if s + snow[x][y] >= S[x][y]:
                    S[x][y] = s + snow[x][y]
                    distance[x][y] = d + 1
    return (S[x][y], distance[x][y])


ms, md = -1, 0
for i in range(N):
    for j in range(N):
        s, d = getDistance(i, j)
        if s >= ms and d >= md:
            ms, md = s, d
print(md)