import sys
sys.setrecursionlimit(5002)

K = int(input())
cache = [0 for _ in range(5001)]
cache[1], cache[2] = 1, 1


def fibo(k):
    if cache[k] != 0:
        return cache[k]
    cache[k] = fibo(k-1) + fibo(k-2)
    return cache[k]


print(fibo(K))
