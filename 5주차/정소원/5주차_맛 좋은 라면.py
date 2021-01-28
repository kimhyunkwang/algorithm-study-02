import sys

n = int(sys.stdin.readline().strip())
powders = list(map(int, sys.stdin.readline().split()))

mn, p = 1000001, (0, 0)
for i in range(n):
    for j in range(i+1, n):
        cur = abs(powders[i] + powders[j])
        if mn > cur:
            mn = cur
            p = (powders[i], powders[j])
print(p[0], p[1])
