# 1번
n, k = map(int, input().split())
sum = 0

for i in range(1,n+1):
    sum = sum + i**k
    
answer = sum % 1000000009
print(answer)


# 2번
N, K = list(map(int, input().split()))
num = 1000000009

def solution(N, K):
    if N == 1:
        return 1

    i, res = 1, 0
    while i <= N:
        res += i**K % num
        i += 2

    if 2**K % num == 0:
        return res % num
    return (res + 2**K * solution(N//2, K) % num) % num


print(solution(N, K))
