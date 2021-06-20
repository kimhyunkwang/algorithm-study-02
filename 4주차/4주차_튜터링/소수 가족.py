# 정소원 코드 추가
# 소수를 판별하는 부분에서, 시간초과 발생 코드 재사용성이 필요해보임(60)
import math
A, B = map(int, input().split())


def prime(n):
    if n == 1:
        return False
    m = int(n**0.5)
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True


def countPrimeFamily(a, b):
    res, k, n = 0, 2, int(b**0.5)
    primes = [False]*(n+1)
    while b**(1/k) >= 2:
        k += 1
    while k >= 2:
        l, r = math.ceil(a**(1/k)), int(b**(1/k))
        for v in range(l, r+1):
            if primes[v]:
                res += 1
            elif prime(v):
                primes[v] = True
                res += 1
        k -= 1
    return res


print(countPrimeFamily(A, B))
# Q. 시간복잡도를 줄일 수 있는 다른 풀이를 알고 싶습니다!
