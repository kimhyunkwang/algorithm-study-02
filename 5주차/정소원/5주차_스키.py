# 프로그래머스 등굣길, 백준 내리막길 문제랑 유사한 듯
import sys
n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cache = [[-1]*m for _ in range(n)]


def get_max_point(x, y):
    if x >= n or y >= m:
        return 0
    if cache[x][y] != -1:
        return cache[x][y]
    cache[x][y] = max(get_max_point(x, y+1),
                      get_max_point(x+1, y)) + matrix[x][y]
    return cache[x][y]


print(get_max_point(0, 0))
