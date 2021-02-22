N = int(input())
crops = [tuple(map(int, input().split())) for _ in range(N)]
cache = [-1] * (N + 1)

for i in range(N - 1, -1, -1):
    t, p = crops[i]
    cache[i + 1], mx = 0, p
    if i + t > N:
        continue
    for j in range(i + t + 1, N + 1):
        mx = max(p + cache[j], mx)
    cache[i + 1] = mx

print(max(cache))