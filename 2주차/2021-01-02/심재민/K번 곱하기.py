# K번 곱하기

# 아직 해결하지 못함 (60점)
# 시간 초과 오류 (테스트 4,5)

N, K = map(int, input().split())

ans = 0

for i in range(1, N+1):
    ans += (i ** K)
    
result = ans % 1000000009

print(result)