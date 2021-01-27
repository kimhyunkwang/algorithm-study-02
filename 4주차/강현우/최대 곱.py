S, K = map(int, input().split())

remain = S%K
lis = [S//K for i in range(K)]

for i in range(remain):
    lis[i] += 1

ans = 1
for i in lis:
    ans *= i
    
print(ans)