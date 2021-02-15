# LDS
import sys

N = int(input())
S = list(map(int, sys.stdin.readline().split()))
cacheLen = [-1] * (N + 1)

res = 1


def lds(start):
    if cacheLen[start] != -1:
        return cacheLen[start]
    cacheLen[start] = 1  # 최소 길이는 1
    for nxt in range(start + 1, N):
        if S[start] > S[nxt]:
            cacheLen[start] = max(lds(nxt) + 1, cacheLen[start])
    return cacheLen[start]


for i in range(N):
    res = max(res, lds(i))
print(res)