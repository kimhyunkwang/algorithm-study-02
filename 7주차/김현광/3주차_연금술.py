import sys

n = int(input())
m = int(input())
materials = list(map(int, sys.stdin.readline().split()))

cnt = 0

for i in range(len(materials) - 1):
    for j in range(i+1, len(materials)):
        if materials[i] + materials[j] == m:
            cnt += 1

print(cnt)