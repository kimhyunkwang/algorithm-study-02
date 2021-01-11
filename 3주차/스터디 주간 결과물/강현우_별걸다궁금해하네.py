n = int(input())
a = list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        ans += abs(a[i] - a[j])

print(ans)

# 한케이스에서 시간초과가 뜹니다. 시간복잡도를 어떻게 줄일수 있는방법이 없을까 질문드려봅니다..!