import sys

n = int(input())
x = list(map(int, sys.stdin.readline().split()))
total = 0

### 방법 1 -> 시간 초과
for i in range(n-1):
    for j in range(i+1, n):
        total += abs(x[i] - x[j])

### 방법 2
x = sorted(x)

for i in range(n-1):
    value = sum(x[i+1:]) - (n-1-i) * x[i]
    total += value


print(total * 2)