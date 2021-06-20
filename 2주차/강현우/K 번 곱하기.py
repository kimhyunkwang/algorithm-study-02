n,k = map(int, input().split())

num = 1000000009
ans = 0

for i in range(1,n+1):
    ans += i**k

print(ans % num)