# 숫자 장식

# 파이썬 내장함수 itertools를 이용한 풀이

from itertools import product

N, M = map(int, input().split())

list_N = [i for i in range(1,N+1)]

for i in product(list_N, repeat=M):
    print(*i)

# 정소원님 풀이

N, M = map(int, input().split())

def combination(n, m, cur):
    if len(cur) == m:
        print(' '.join(cur))
        return
    for i in range(1, n+1):
        combination(n, m, cur+[str(i)])
        
combination(N, M, [])