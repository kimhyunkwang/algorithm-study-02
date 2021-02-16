N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
cache = [[-1] * M for _ in range(N)]


def getMaxPatient(x, y):
    if x >= N or y >= M:
        return 0
    if cache[x][y] != -1:
        return cache[x][y]
    cache[x][y] = (
        max(
            getMaxPatient(x + 1, y),
            getMaxPatient(x, y + 1),
            getMaxPatient(x + 1, y + 1),
        )
        + matrix[x][y]
    )
    return cache[x][y]


print(getMaxPatient(0, 0))
