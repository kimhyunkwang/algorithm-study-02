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

# Q. 반복형 DP (bottom-up) 방식으로 푸는 방법도 있을까요 ?
# Q. 보통 DP에 접근할 때 재귀로 많이 풀려고 하는 편인데, 파이썬에서는 어떤 식으로 접근하는게 더 유리할까요..?
