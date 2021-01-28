import sys
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
cache = [-1 for _ in range(n+1)]
cache[n] = 1


def num(cur):
    if cur > n:
        return 0
    if cache[cur] != -1:
        return cache[cur]
    cache[cur] = (num(cur+1) + num(cur+m)) % 1000007
    return cache[cur]


print(num(0))
