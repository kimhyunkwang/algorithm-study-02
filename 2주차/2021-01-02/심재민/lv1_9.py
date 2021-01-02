# K번 곱하기

N, K = map(int, input().split())

ans = 0

for i in range(1, N+1):
    ans += (i ** K)
    
result = ans % 1000000009

print(result)