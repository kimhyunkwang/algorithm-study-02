N = int(input())
M = int(input())
ingre = list(map(int, input().split()))

ans = 0
for i in ingre:
    if (M-i) in ingre:
        ans += 1

print(ans//2)