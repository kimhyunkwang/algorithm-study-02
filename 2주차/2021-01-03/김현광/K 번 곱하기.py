n, k = map(int, input().split())
SUM = 0

for i in range(1, n+1):
    SUM += i**k

answer = SUM % (10**9 + 9)
print(answer)