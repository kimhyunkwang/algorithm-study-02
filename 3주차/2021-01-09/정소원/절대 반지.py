hatter, N = input(), int(input())
rings = [input() for _ in range(N)]

res = 0
for i in range(len(rings)):
    ring = rings[i]*2
    if hatter in ring:
        res += 1
print(res)
