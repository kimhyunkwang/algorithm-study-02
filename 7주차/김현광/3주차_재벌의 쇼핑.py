import sys

N, S = map(int, input().split())
products = list(map(int, sys.stdin.readline().split()))

counts = []
for i in range(N):
    total = products[i]
    count = 1
    for j in range(i+1, N):
        if total >= S:
            counts.append(count)
            break
        total += products[j]
        count += 1
        
if len(counts) == 0:
    print(0)
else:
    print(min(counts))