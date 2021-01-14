N,K = map(int, input().split())
ans = 0

while N not in range(K-N,K+N):
    ans += (K % 3) + 1
    K = K // 3

print(abs(K-N)+ans)