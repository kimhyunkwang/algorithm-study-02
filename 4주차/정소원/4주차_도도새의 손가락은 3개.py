# D(n) = D(n-1)+D(n-2)+D(n-3) (n>3)
# D(1) = 1, D(2) = 2, D(3) = 4
N = int(input())
cache = [-1 for _ in range(1000001)]
cache[1], cache[2], cache[3] = 1, 2, 4
# 방법1: 반복적 동적계획법 => 파이썬은 재귀 허용 범위가 짧은 편이어서 반복문이 메모리면에서는 더 효율적인듯
i = 4
while cache[N] == -1:
    cache[i] = (cache[i-1]+cache[i-2]+cache[i-3]) % 123456
    i += 1
print(cache[N])

# 방법2: 재귀적 동적계획법(80) => 파이썬 재귀 한계점 때문에 스택 메모리 초과되서 참조 에러 발생하는 듯 재귀를 더 줄이는 방법은 모르겠음
# import sys
# sys.setrecursionlimit(1000000)

# def solution(n):
#     # print(n)
#     if cache[n] != -1:
#         return cache[n]
#     cache[n] = (solution(n-1)+solution(n-2)+solution(n-3)) % 123456
#     return cache[n]

# print(solution(N))
