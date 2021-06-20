N = int(input())
pyramid = [list(map(int, input().split())) for _ in range(N)]
cache = [[-1] * (v + 1) for v in range(N)]


def maxEscapeTime(x, y):
    if x >= N or y >= N:
        return 0
    if cache[x][y] != -1:
        return cache[x][y]
    cache[x][y] = (
        max(maxEscapeTime(x + 1, y), maxEscapeTime(x + 1, y + 1)) + pyramid[x][y]
    )
    return cache[x][y]


print(maxEscapeTime(0, 0))
