n = int(input())
b = list(map(int, input().split()))
a = []
SUM = 0

for i in range(n):
    a.append(b[i] * (i + 1) - SUM)
    SUM += a[i]
    print(a[i], end=' ')